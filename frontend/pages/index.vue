<template>
	<Hero />
	<div class="container mx-auto px-2">
		<div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-6">
			<div
				class="p-4 md:p-8 bg-base-100 rounded-lg shadow-xl border-4 border-base-300 flex flex-col flex-none"
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
							class="select select-bordered w-full bg-base-200"
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
							class="input input-bordered w-full bg-base-200"
							placeholder="Enter Year (e.g., 2025)"
							v-model="year"
							required
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
							class="input input-bordered w-full bg-base-200"
							placeholder="Enter Longitude"
							v-model="longitude"
							@input="updateMapCenter"
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
							class="input input-bordered w-full bg-base-200"
							placeholder="Enter Latitude"
							v-model="latitude"
							@input="updateMapCenter"
							required
						/>
					</div>

					<!-- Submit Button -->
					<div class="form-control md:col-span-2">
						<button type="submit" class="btn btn-primary w-full">Submit</button>
					</div>
				</form>
			</div>
			<LMap
				:zoom="zoom"
				:center.sync="mapCenter"
				@dragend="updateCoordinatesFromMap"
				:use-global-leaflet="false"
				class="bg-base-100 rounded-lg shadow-xl border-4 border-base-300 aspect-video"
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
</template>

<script>
	export default {
		data() {
			return {
				month: "",
				year: "",
				longitude: 0,
				latitude: 0,
				zoom: 5,
				mapCenter: [0, 0], // Map center
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
			handleSubmit() {
				console.log("Form Submitted", {
					month: this.month,
					year: this.year,
					longitude: this.longitude,
					latitude: this.latitude,
				});
				// TODO: Make API request to the backend
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
