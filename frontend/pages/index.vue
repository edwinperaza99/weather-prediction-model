<template>
	<div class="p-6 bg-base-100 rounded-lg shadow-md max-w-4xl mx-auto">
		<h1 class="text-4xl font-bold text-center mb-8">
			Weather Prediction Model
		</h1>

		<!-- Weather Prediction Form -->
		<form
			@submit.prevent="handleSubmit"
			class="grid grid-cols-1 md:grid-cols-2 gap-6"
		>
			<!-- Month -->
			<div class="form-control">
				<label for="month" class="label">
					<span class="label-text font-medium">Month</span>
				</label>
				<select
					id="month"
					class="select select-bordered w-full"
					v-model="month"
					required
				>
					<option disabled selected>Select Month</option>
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
					<span class="label-text font-medium">Year</span>
				</label>
				<input
					type="number"
					id="year"
					class="input input-bordered w-full"
					placeholder="Enter Year (e.g., 2025)"
					v-model="year"
					required
				/>
			</div>

			<!-- Longitude -->
			<div class="form-control">
				<label for="longitude" class="label">
					<span class="label-text font-medium">Longitude</span>
				</label>
				<input
					type="number"
					id="longitude"
					class="input input-bordered w-full"
					placeholder="Enter Longitude"
					v-model="longitude"
					required
				/>
			</div>

			<!-- Latitude -->
			<div class="form-control">
				<label for="latitude" class="label">
					<span class="label-text font-medium">Latitude</span>
				</label>
				<input
					type="number"
					id="latitude"
					class="input input-bordered w-full"
					placeholder="Enter Latitude"
					v-model="latitude"
					required
				/>
			</div>

			<!-- Submit Button -->
			<div class="form-control md:col-span-2">
				<button type="submit" class="btn btn-primary w-full">Submit</button>
			</div>
		</form>
	</div>
</template>

<script>
	export default {
		data() {
			return {
				month: "",
				year: "",
				longitude: "",
				latitude: "",
			};
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
		},
	};
</script>
