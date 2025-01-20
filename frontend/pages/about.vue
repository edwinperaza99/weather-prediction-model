<template>
	<div id="about" class="pt-6 md:pt-16 bg-base-100">
		<div class="container mx-auto px-2">
			<!-- Header Section -->
			<section
				class="flex flex-col md:flex-row items-center justify-between mb-12 gap-1"
			>
				<header class="md:w-3/5">
					<h1 class="text-6xl font-bold text-primary">Weatheria</h1>
					<div class="flex items-center gap-2 mb-4">
						<p class="text-xs text-secondary">ウェザリア (Wezaria)</p>
						<!-- <button
							class="inline"
							@click="playPronunciation"
							aria-label="Play pronunciation"
						>
							🔊
						</button> -->
					</div>
					<p class="text-content leading-relaxed">
						The name is inspired by a fictional sky island from the show
						<em>One Piece</em>, a place known for its innovative connection to
						weather. This inspiration aligns with the project's mission to merge
						advanced machine learning with climate data, delivering precise
						predictions of Earth surface temperatures and meaningful climate
						insights.
					</p>
				</header>
				<figure class="md:w-1/3">
					<img
						src="~/assets/images/weatheria.png"
						alt="Weatheria illustration"
						class="drop-shadow-2xl illustration"
					/>
				</figure>
			</section>

			<!-- Project Overview -->
			<section class="mb-12">
				<header>
					<h2 class="text-3xl font-semibold text-secondary mb-4">
						What Does Weatheria Do<span class="text-accent">?</span>
					</h2>
				</header>
				<p class="text-content leading-relaxed">
					Weatheria predicts Earth surface temperatures using advanced machine
					learning techniques. By analyzing historical climate data, it
					forecasts global warming trends based on spatial (latitude, longitude)
					and temporal (year, month) features. The insights aim to contribute to
					a deeper understanding of climate change's impact and help build
					resilience against its effects.
				</p>
			</section>

			<!-- Technical Details -->
			<section class="mb-12">
				<header>
					<h2 class="text-3xl font-semibold text-secondary mb-4">
						How It Was Built<span class="text-accent">.</span>
					</h2>
				</header>
				<ul class="list-disc list-inside text-content leading-relaxed">
					<li>
						<strong>Frontend:</strong> Built using Nuxt.js with TailwindCSS for
						styling and extended with DaisyUI components for a modern,
						responsive design. The frontend is deployed on Vercel.
					</li>
					<li>
						<strong>Backend:</strong> Hosted on Google Cloud's Virtual Machine
						(VM) and containerized using Docker for easy scalability and
						reliable deployment. The backend was developed with FastAPI,
						responsible for serving predictions from pre-trained machine
						learning models.
					</li>
					<li>
						<strong>Machine Learning:</strong> The models were built using
						Python and the Scikit-learn library. Four algorithms were used:
						Random Forest, K-Nearest Neighbor (KNN), Support Vector Regression
						(SVR), and Linear Regression. The Random Forest model achieved the
						highest accuracy with an R² score of
						<span class="text-accent">0.9857</span>.
					</li>
					<li>
						<strong>Images and Illustrations:</strong> The visuals used in the
						project are sourced from
						<a
							href="https://storyset.com/"
							class="text-primary hover:text-accent"
							target="_blank"
							rel="noopener noreferrer"
							>Storyset</a
						>, under their license agreement. Special thanks for providing
						high-quality illustrations to enhance the user interface.
					</li>
				</ul>
			</section>

			<!-- Dataset and Data Handling -->
			<section class="mb-12">
				<header>
					<h2 class="text-3xl font-semibold text-secondary mb-4">
						Dataset and Data Handling<span class="text-accent">.</span>
					</h2>
				</header>
				<p class="text-content leading-relaxed mb-4">
					The dataset used in this project is sourced from the
					<a
						href="https://berkeleyearth.org/data/"
						class="text-primary hover:text-accent"
						target="_blank"
						rel="noopener noreferrer"
						>Berkeley Earth Surface Temperature</a
					>
					repository, a trusted resource for historical climate data. It
					includes records of average land temperatures collected globally,
					along with metadata such as date, latitude, longitude, and uncertainty
					levels. To ensure data quality:
				</p>
				<ul class="list-disc list-inside text-content leading-relaxed mb-4">
					<li>
						Records prior to 1870 were excluded due to data incompleteness.
					</li>
					<li>
						Missing temperature values were removed to maintain dataset
						integrity.
					</li>
					<li>
						Features such as year, month, latitude, and longitude were carefully
						extracted for model training.
					</li>
				</ul>
				<p class="text-content leading-relaxed">
					These steps resulted in a clean and structured dataset, allowing the
					models to effectively capture spatial and temporal patterns in global
					temperature changes.
				</p>
			</section>

			<!-- Machine Learning Models -->
			<section class="mb-12">
				<header>
					<h2 class="text-3xl font-semibold text-secondary mb-4">
						Machine Learning Models and Results<span class="text-accent"
							>.</span
						>
					</h2>
				</header>
				<p class="text-content leading-relaxed mb-4">
					Four machine learning algorithms were employed to analyze the data:
					Random Forest, K-Nearest Neighbor (KNN), Support Vector Regression
					(SVR), and Linear Regression. Each model was evaluated using metrics
					such as Mean Absolute Error (MAE), Median Absolute Error (MedAE), Mean
					Squared Error (MSE), Root Mean Squared Error (RMSE), and R² scores.
					Random Forest emerged as the most accurate model with an R² score of
					0.9857.
				</p>

				<!-- Table -->
				<div class="overflow-x-auto">
					<table class="table table-zebra w-full">
						<thead class="bg-base-300">
							<tr>
								<th>Model</th>
								<th>MAE</th>
								<th>MedAE</th>
								<th>MSE</th>
								<th>RMSE</th>
								<th>R² Score</th>
							</tr>
						</thead>
						<tbody>
							<tr>
								<td>Random Forest M1</td>
								<td>0.7749</td>
								<td>0.5028</td>
								<td>1.3258</td>
								<td>1.1514</td>
								<td>0.9857</td>
							</tr>
							<tr>
								<td>Random Forest M2</td>
								<td>0.7741</td>
								<td>0.5005</td>
								<td>1.3284</td>
								<td>1.1526</td>
								<td>0.9857</td>
							</tr>
							<tr>
								<td>KNN M1</td>
								<td>1.1471</td>
								<td>0.7736</td>
								<td>2.7303</td>
								<td>1.6524</td>
								<td>0.9705</td>
							</tr>
							<tr>
								<td>KNN M2</td>
								<td>5.2274</td>
								<td>3.4834</td>
								<td>52.9441</td>
								<td>7.2763</td>
								<td>0.4287</td>
							</tr>
							<tr>
								<td>SVR M1</td>
								<td>2.0081</td>
								<td>1.4573</td>
								<td>7.6086</td>
								<td>2.7584</td>
								<td>0.9179</td>
							</tr>
							<tr>
								<td>SVR M2</td>
								<td>5.9241</td>
								<td>4.9484</td>
								<td>58.0018</td>
								<td>7.6159</td>
								<td>0.3741</td>
							</tr>
							<tr>
								<td>SVR M3</td>
								<td>6.8501</td>
								<td>5.1715</td>
								<td>84.9333</td>
								<td>9.2159</td>
								<td>0.0835</td>
							</tr>
							<tr>
								<td>Linear SVR M1</td>
								<td>6.8504</td>
								<td>5.1649</td>
								<td>84.9363</td>
								<td>9.2161</td>
								<td>0.0835</td>
							</tr>
							<tr>
								<td>Linear Regression M1</td>
								<td>7.0842</td>
								<td>6.0307</td>
								<td>79.7846</td>
								<td>8.9322</td>
								<td>0.1391</td>
							</tr>
							<tr>
								<td>Linear Regression M2</td>
								<td>7.1300</td>
								<td>6.0911</td>
								<td>80.7002</td>
								<td>8.9833</td>
								<td>0.1292</td>
							</tr>
						</tbody>
					</table>
				</div>
			</section>

			<!-- Results -->
			<section class="mb-12">
				<header>
					<h2 class="text-3xl font-semibold text-secondary mb-4">
						Key Results<span class="text-accent">.</span>
					</h2>
				</header>
				<p class="text-content leading-relaxed mb-6">
					The project analyzed global climate data to predict temperature trends
					with remarkable accuracy. Below is a summary of the performance of the
					models:
				</p>
				<div class="overflow-x-auto">
					<table class="table w-full">
						<thead class="bg-base-300 z-10">
							<tr>
								<th>Model</th>
								<th>Configuration</th>
								<th>R² Score</th>
							</tr>
						</thead>
						<tbody>
							<tr>
								<td>Random Forest</td>
								<td>Final Features</td>
								<td>0.9857</td>
							</tr>
							<tr>
								<td>KNN</td>
								<td>Final Features</td>
								<td>0.9706</td>
							</tr>
							<tr>
								<td>SVR</td>
								<td>RBF Kernel</td>
								<td>0.9179</td>
							</tr>
							<tr>
								<td>Linear Regression</td>
								<td>Final Features</td>
								<td>0.1391</td>
							</tr>
						</tbody>
					</table>
				</div>
			</section>

			<!-- About Me -->
			<section class="pb-12">
				<header>
					<h2 class="text-3xl font-semibold text-secondary mb-4">
						About Me<span class="text-accent">.</span>
					</h2>
				</header>
				<p class="text-content leading-relaxed">
					Hello! I'm Edwin Peraza, a passionate software developer with a strong
					focus on leveraging technology to solve impactful problems. This
					project, a machine learning-powered weather prediction system, was
					developed during my time at California State University, Fullerton.
					While it was a class project, I contributed the majority of the work,
					including the implementation, research, and deployment.
				</p>
			</section>
		</div>
	</div>
</template>

<script>
	import { gsap } from "gsap";
	import { ScrollTrigger } from "gsap/ScrollTrigger";

	gsap.registerPlugin(ScrollTrigger);

	export default {
		mounted() {
			const timeline = gsap.timeline({
				scrollTrigger: {
					trigger: "#about", // The main container
					start: "top center",
					end: "bottom center",
					scrub: true,
				},
			});

			// Animate the header (Weatheria text)
			gsap.from(".text-primary", {
				y: -50,
				opacity: 0,
				duration: 1.5,
				ease: "power4.out",
			});

			// Animate sub-header (Wezaria and description)
			gsap.from(".text-secondary, .text-content", {
				x: -100,
				opacity: 0,
				duration: 1.2,
				stagger: 0.3,
				ease: "power3.inOut",
			});

			// Stagger images and other sections
			timeline.fromTo(
				".about-section",
				{ opacity: 0, y: 50 },
				{ opacity: 1, y: 0, duration: 1.5, stagger: 0.2, ease: "power2.out" }
			);

			// Parallax effect for the Weatheria illustration
			gsap.to(".illustration", {
				y: -30,
				duration: 2,
				ease: "power2.out",
				scrollTrigger: {
					trigger: ".illustration",
					start: "top 80%",
					scrub: true,
				},
			});
		},
	};
</script>
