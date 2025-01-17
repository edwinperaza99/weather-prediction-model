<template>
	<div class="bg-base-100">
		<div class="container mx-auto pt-6 min-h-screen" id="predictions">
			<h3 class="text-4xl font-semibold mb-4 text-primary">
				Predictions from My Models<span class="text-secondary">.</span>
			</h3>
			<p class="text-sm text-base-content">
				The predictions below show estimated Earth surface temperatures for the
				selected time and location. This does not represent air temperature or
				daily weather conditions.
			</p>
			<div class="flex flex-col md:flex-row items-center justify-between">
				<div class="md:w-2/5">
					<h3 class="text-2xl font-bold text-center text-primary mt-3">
						Results
					</h3>
					<ul class="timeline timeline-vertical">
						<li v-for="(modelName, index) in modelNames" :key="index">
							<hr v-if="index > 0" class="bg-accent" />
							<div class="timeline-start timeline-box">
								{{ modelName }}
							</div>
							<div class="timeline-middle">
								<svg
									xmlns="http://www.w3.org/2000/svg"
									viewBox="0 0 20 20"
									fill="currentColor"
									class="text-primary h-5 w-5"
								>
									<path
										fill-rule="evenodd"
										d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
										clip-rule="evenodd"
									/>
								</svg>
							</div>
							<div class="timeline-end timeline-box">
								<span v-if="predictions?.[index]">
									{{
										convertTemperature(predictions[index].prediction).toFixed(2)
									}}
									<span v-if="selectedUnit === 'C'">°C</span>
									<span v-else-if="selectedUnit === 'F'">°F</span>
									<span v-else>K</span>
								</span>
								<div v-else-if="loading">Loading predictions...</div>
								<span v-else> Awaiting input... </span>
							</div>
							<hr v-if="index < 3" class="bg-accent" />
						</li>
						<li>
							<hr class="bg-accent" />
							<div class="timeline-middle">
								<p class="font-accent font-thin text-center text-sm">
									Note: Predictions from the Random Forest model are currently
									unavailable due to limited storage space on the virtual
									machine. Other models are unaffected and available for
									testing.
								</p>
							</div>
						</li>
					</ul>
					<div class="flex items-center justify-center gap-2 my-4">
						<label
							for="unit-selector"
							class="text-sm font-medium text-secondary"
						>
							Temperature Unit:
						</label>
						<select
							id="unit-selector"
							v-model="selectedUnit"
							class="select select-bordered select-sm select-secondary"
						>
							<option value="C">Celsius (°C)</option>
							<option value="F">Fahrenheit (°F)</option>
							<option value="K">Kelvin (K)</option>
						</select>
					</div>
				</div>
				<div class="w-full md:w-3/5">
					<First />
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	export default {
		name: "PredictionTimeline",
		props: {
			predictions: {
				type: Array,
				required: false,
				default: () => [], // Default to an empty array
			},
		},
		data() {
			return {
				// Fixed list of model names
				modelNames: ["KNN", "Linear Regression", "Random Forest"],
				selectedUnit: "C",
			};
		},
		methods: {
			convertTemperature(value) {
				if (this.selectedUnit === "F") {
					// Celsius to Fahrenheit: (Celsius * 9/5) + 32
					return (value * 9) / 5 + 32;
				} else if (this.selectedUnit === "K") {
					// Celsius to Kelvin: Celsius + 273.15
					return value + 273.15;
				}
				// Default to Celsius
				return value;
			},
		},
	};
</script>
