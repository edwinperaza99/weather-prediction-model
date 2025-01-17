<template>
	<Hero />
	<div class="border-b-2 border-accent">
		<div class="container mx-auto px-4 py-6 md:py-8" id="predict-form">
			<h2 class="text-primary text-4xl font-semibold mb-1">
				Test the models<span class="text-secondary">.</span>
			</h2>
			<p class="mb-4 text-sm text-base-content">
				Enter a location and time to see temperature predictions from models I
				built using machine learning. The results show how each model performs
				with real-world inputs.
			</p>
			<div class="grid grid-cols-1 md:grid-cols-2 gap-3 md:gap-6">
				<div
					class="p-4 md:p-8 bg-base-100 rounded-lg shadow-xl border-2 border-accent flex flex-col flex-none"
				>
					<h2
						class="text-3xl md:text-4xl font-bold text-center mb-4 text-primary"
					>
						Predict
					</h2>

					<form
						@submit.prevent="handleSubmit"
						class="grid grid-cols-1 md:grid-cols-2 gap-4"
					>
						<!-- Month -->
						<div class="form-control">
							<label for="month" class="label">
								<span class="label-text font-medium text-secondary">Month</span>
							</label>
							<select
								id="month"
								class="select select-bordered select-accent w-full bg-base-200"
								v-model="month"
								required
							>
								<option value="" disabled selected>Select Month</option>
								<option value="1">January</option>
								<option value="2">February</option>
								<option value="3">March</option>
								<option value="4">April</option>
								<option value="5">May</option>
								<option value="6">June</option>
								<option value="7">July</option>
								<option value="8">August</option>
								<option value="9">September</option>
								<option value="10">October</option>
								<option value="11">November</option>
								<option value="12">December</option>
							</select>
						</div>

						<!-- Year -->
						<div class="form-control">
							<label for="year" class="label">
								<span class="label-text font-medium text-secondary">Year</span>
							</label>
							<input
								type="number"
								id="year"
								class="input input-bordered input-accent w-full bg-base-200"
								placeholder="Enter Year (e.g., 2025)"
								v-model="year"
								required
								min="1000"
								max="9999"
								inputmode="numeric"
							/>
						</div>

						<!-- Longitude -->
						<div class="form-control">
							<label for="longitude" class="label">
								<span class="label-text font-medium text-secondary"
									>Longitude</span
								>
							</label>
							<input
								type="number"
								id="longitude"
								class="input input-bordered input-accent w-full bg-base-200"
								placeholder="Enter Longitude"
								v-model="longitude"
								@input="updateMapCenter"
								step="any"
								required
							/>
						</div>

						<!-- Latitude -->
						<div class="form-control">
							<label for="latitude" class="label">
								<span class="label-text font-medium text-secondary"
									>Latitude</span
								>
							</label>
							<input
								type="number"
								id="latitude"
								class="input input-bordered input-accent w-full bg-base-200"
								placeholder="Enter Latitude"
								v-model="latitude"
								@input="updateMapCenter"
								step="any"
								required
							/>
						</div>

						<!-- Submit Button -->
						<div class="form-control md:col-span-2">
							<button type="submit" class="btn btn-primary w-full">
								Submit
							</button>
						</div>
					</form>
				</div>
				<LMap
					:zoom="zoom"
					:center.sync="mapCenter"
					@dragend="updateCoordinatesFromMap"
					:use-global-leaflet="false"
					class="bg-base-100 rounded-lg shadow-xl border-2 border-accent aspect-video"
				>
					<LTileLayer
						url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
						attribution='&amp;copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors'
						layer-type="base"
						name="OpenStreetMap"
					/>
				</LMap>
			</div>
		</div>
	</div>
	<!-- Predictions Timeline -->
	<Predictions
		:predictions="predictions"
		:skeletonCount="3"
		:loading="loading"
	/>
</template>

<script>
	export default {
		data() {
			return {
				month: "",
				year: "",
				longitude: -0.1276, // Default: London (UK)
				latitude: 51.5074, // Default: London (UK)
				zoom: 10,
				mapCenter: [51.5074, -0.1276], // Default: London (UK)
				predictions: null, // To store API response
				loading: false, // Loading state
				error: null, // Error message
			};
		},
		watch: {
			latitude(newLat) {
				this.mapCenter = [newLat, this.longitude];
			},
			longitude(newLng) {
				this.mapCenter = [this.latitude, newLng];
			},
		},
		methods: {
			async setUserLocation() {
				if (navigator.geolocation) {
					navigator.geolocation.getCurrentPosition(
						(position) => {
							this.latitude = position.coords.latitude;
							this.longitude = position.coords.longitude;
							this.mapCenter = [this.latitude, this.longitude];
						},
						() => {
							// If the user denies access, the default (Los Angeles) is used.
							console.warn(
								"Geolocation access denied. Using default location."
							);
						}
					);
				} else {
					console.warn("Geolocation is not supported by this browser.");
				}
			},
			async handleSubmit() {
				console.log("Form Submitted", {
					month: this.month,
					year: this.year,
					longitude: this.longitude,
					latitude: this.latitude,
				});
				try {
					// Create a JSON object with the form data
					const requestData = {
						year: this.year,
						latitude: this.latitude,
						longitude: this.longitude,
						month: this.month,
					};

					// Send the data as a JSON payload to the API
					const response = await fetch("http://34.83.214.37:9000/predict", {
						method: "POST",
						headers: {
							"Content-Type": "application/json", // Set Content-Type to application/json
						},
						body: JSON.stringify(requestData), // Convert the data to JSON format
					});

					if (!response.ok) {
						const errorData = await response.json();
						throw new Error(errorData.error || "Failed to fetch predictions");
					}

					const data = await response.json();
					this.predictions = data.predictions;
					console.log(
						"Predictions:",
						JSON.parse(JSON.stringify(this.predictions))
					);

					// Scroll to predictions section
					this.$nextTick(() => {
						const predictionsSection = document.getElementById("predictions");
						predictionsSection?.scrollIntoView({ behavior: "smooth" });
					});
				} catch (error) {
					console.error("Error during API call:", error);
					this.error = error.message;
				} finally {
					this.loading = false;
				}
			},
			updateMapCenter() {
				this.mapCenter = [this.latitude, this.longitude];
			},
			updateCoordinatesFromMap(event) {
				const { lat, lng } = event.target.getCenter();
				this.latitude = lat;
				this.longitude = lng;
			},
		},
	};
</script>
