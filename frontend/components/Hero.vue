<template>
	<div class="hero bg-base-100 border-b-2 border-accent min-h-viewport">
		<div class="text-center hero-content flex flex-col gap-0">
			<div class="max-w-lg">
				<h1 ref="title" class="mb-4 text-6xl font-black text-primary">
					Weatheria
				</h1>
				<p
					ref="description"
					class="mb-6 text-lg text-content font-light leading-tight"
				>
					Leverage the power of advanced machine learning algorithms to
					accurately predict weather patterns. Start exploring today!
				</p>
				<div class="flex justify-center gap-4">
					<a
						ref="button1"
						href="#predict-form"
						class="btn btn-accent text-white hover:text-white/80 text-lg hover:scale-105 transition-transform"
					>
						Try It Out
					</a>
					<a
						ref="button2"
						href="/about"
						class="btn btn-secondary text-white hover:text-white/80 text-lg hover:scale-105 transition-transform"
					>
						Learn More
					</a>
				</div>
			</div>
			<Second />
		</div>
	</div>
</template>

<script>
	import { gsap } from "gsap";

	export default {
		setup() {
			const title = ref(null);
			const description = ref(null);
			const button1 = ref(null);
			const button2 = ref(null);

			onMounted(() => {
				// Animate the title
				gsap.fromTo(
					title.value,
					{ y: -50, opacity: 0 },
					{ y: 0, opacity: 1, duration: 1, ease: "power3.inOut" }
				);

				// Animate the description
				gsap.fromTo(
					description.value,
					{ y: 50, opacity: 0 },
					{ y: 0, opacity: 1, delay: 0.5, duration: 1, ease: "power3.inOut" }
				);

				// Animate the buttons
				gsap.fromTo(
					button1.value,
					{ x: -50, opacity: 0 },
					{ x: 0, opacity: 1, delay: 1, duration: 1, ease: "power3.inOut" }
				);

				gsap.fromTo(
					button2.value,
					{ x: 50, opacity: 0 },
					{ x: 0, opacity: 1, delay: 1, duration: 1, ease: "power3.inOut" }
				);
			});

			return {
				title,
				description,
				button1,
				button2,
			};
		},
	};
</script>
