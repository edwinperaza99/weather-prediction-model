<template>
	<div class="hero bg-base-100 border-b-2 border-accent min-h-viewport">
		<div class="text-center hero-content flex flex-col gap-0">
			<div class="max-w-lg">
				<h1 class="mb-4 text-6xl font-black text-primary">Weatheria</h1>
				<p class="mb-6 text-lg text-content font-light leading-tight">
					Leverage the power of advanced machine learning algorithms to
					accurately predict weather patterns. Start exploring today!
				</p>
				<div class="flex justify-center gap-4">
					<a
						href="#predict-form"
						class="btn btn-accent text-white hover:text-white/80 text-lg hover:scale-105 transition-transform"
					>
						Get Started
					</a>
					<a
						href="/about"
						class="btn btn-secondary text-white hover:text-white/80 text-lg hover:scale-105 transition-transform"
					>
						Learn More
					</a>
				</div>
			</div>
			<First />
		</div>
	</div>
</template>
