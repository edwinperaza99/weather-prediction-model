<template>
	<NuxtRouteAnnouncer />
	<NuxtLayout>
		<NuxtLoadingIndicator />
		<NuxtPage />
	</NuxtLayout>
</template>

<script setup lang="ts">
	useHead({
		title: "Weatheria",
		meta: [
			{
				name: "description",
				content:
					"Predict Earth’s surface temperatures with advanced machine learning models. Analyze historical climate data and forecast spatial and temporal trends.",
			},
			{
				name: "keywords",
				content:
					"earth temperature prediction, climate modeling, surface temperature, Weatheria, machine learning climate app",
			},
			{ name: "author", content: "Edwin Peraza" },

			{
				property: "og:title",
				content: "Weatheria - Earth Surface Temperature Predictor",
			},
			{
				property: "og:description",
				content:
					"Explore global climate trends and predict Earth’s surface temperatures using cutting-edge machine learning algorithms.",
			},
			{ property: "og:type", content: "website" },
			{ property: "og:url", content: "https://www.weatheria.com" },
			{ name: "twitter:card", content: "summary_large_image" },
			{
				name: "twitter:title",
				content: "Weatheria - Earth Surface Temperature Predictor",
			},
			{
				name: "twitter:description",
				content:
					"Discover insights into Earth’s surface temperature trends with Weatheria’s machine learning-powered predictions.",
			},
		],
	});
</script>
