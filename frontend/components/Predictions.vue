<template>
	<div class="mt-6 min-h-screen" id="predictions">
		<h3 class="text-2xl font-bold text-center mb-4 text-primary">
			Predictions
		</h3>
		<ul class="timeline timeline-vertical">
			<li v-for="(modelName, index) in modelNames" :key="index">
				<hr v-if="index > 0" class="bg-accent" />
				<div class="timeline-start">
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
						{{ predictions[index].prediction.toFixed(2) }}
					</span>
					<span v-else> Awaiting input... </span>
				</div>
				<hr v-if="index < 2" class="bg-accent" />
			</li>
		</ul>
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
				modelNames: ["KNN", "Random Forest", "Linear Regression"],
			};
		},
	};
</script>
