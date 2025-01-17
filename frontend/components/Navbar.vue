<template>
    <header class="bg-base-300 border-b-2 border-accent">
        <nav class="navbar container mx-auto justify-between px-2">
            <!-- Left Section -->
            <div class="navbar-start">
                <a href="https://github.com/edwinperaza99/weather-prediction-model" rel="noopener noreferrer"
                    target="_blank" class="flex items-center space-x-2 hover:text-primary transition-colors menu">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="w-6 h-6" viewBox="0 0 24 24">
                        <path
                            d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.726-4.042-1.612-4.042-1.612-.546-1.387-1.333-1.757-1.333-1.757-1.09-.744.083-.729.083-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.419-1.305.762-1.605-2.665-.305-5.466-1.333-5.466-5.93 0-1.31.469-2.381 1.236-3.221-.123-.303-.536-1.524.117-3.176 0 0 1.008-.322 3.3 1.23a11.52 11.52 0 013.003-.404 11.52 11.52 0 013.003.404c2.292-1.552 3.3-1.23 3.3-1.23.653 1.653.24 2.874.118 3.176.768.84 1.236 1.911 1.236 3.221 0 4.609-2.804 5.624-5.476 5.921.431.372.815 1.102.815 2.221 0 1.606-.015 2.899-.015 3.293 0 .321.218.694.825.576C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12z" />
                    </svg>
                </a>
                <!-- Theme Dropdown -->
            </div>

            <!-- Right Section -->
            <div class="navbar-end">
                <!-- Desktop navbar -->
                <div class="hidden md:flex text-base-content">
                    <ul class="menu menu-horizontal">
                        <li>
                            <nuxt-link to="/" class="hover:text-primary transition-colors duration-300">
                                Home
                            </nuxt-link>
                        </li>
                        <li>
                            <nuxt-link to="/about" class="hover:text-primary transition-colors duration-300">
                                About
                            </nuxt-link>
                        </li>
                        <li class="dropdown dropdown-hover dropdown-end text-primary">
                            <label tabindex="0" class="btn btn-primary btn-sm">
                                Theme
                                <svg width="12px" height="12px" class="inline-block h-3 w-3 fill-current ml-1"
                                    xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2048 2048">
                                    <path d="M1799 349l242 241-1017 1017L7 590l242-241 775 775 775-775z"></path>
                                </svg>
                            </label>
                            <ul tabindex="0"
                                class="dropdown-content menu bg-base-200 shadow-md border border-accent rounded-box w-52 p-2">
                                <li v-for="theme in themes" :key="theme" @click="changeTheme(theme)">
                                    <button class="btn btn-ghost btn-sm w-full" :class="{
                                        'text-accent': theme === currentTheme, // Add text-accent if selected
                                    }">
                                        {{ theme }}
                                    </button>
                                </li>
                            </ul>
                        </li>
                    </ul>
                </div>

                <!-- mobile navbar -->
                <div class="md:hidden text-content">
                    <!-- Hamburger Menu Button -->
                    <button class="btn btn-ghost" @click="isMobileMenuOpen = !isMobileMenuOpen">
                        <svg v-if="!isMobileMenuOpen" xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none"
                            viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M4 6h16M4 12h8m-8 6h16" />
                        </svg>
                        <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24"
                            stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M6 18L18 6M6 6l12 12" />
                        </svg>
                    </button>

                </div>
            </div>
        </nav>
        <!-- Mobile Menu Items -->
        <div v-if="isMobileMenuOpen" class="pb-4 px-2">
            <ul class="space-y-2 text-center text-content">
                <li>
                    <nuxt-link to="/" class="block hover:text-primary transition-colors">
                        Home
                    </nuxt-link>
                </li>
                <li>
                    <nuxt-link to="/about" class="block hover:text-primary transition-colors">
                        About
                    </nuxt-link>
                </li>
                <li>
                <li class="dropdown dropdown-hover text-primary">
                    <label tabindex="0" class="btn btn-primary btn-sm">
                        Select Theme
                        <!-- <svg
									width="12px"
									height="12px"
									class="inline-block h-3 w-3 fill-current ml-1"
									xmlns="http://www.w3.org/2000/svg"
									viewBox="0 0 2048 2048"
								>
									<path
										d="M1799 349l242 241-1017 1017L7 590l242-241 775 775 775-775z"
									></path>
								</svg> -->
                    </label>
                    <ul tabindex="0" class="dropdown-content menu bg-base-200 shadow-md rounded-box w-52 p-2 z-[1000]">
                        <li v-for="theme in themes" :key="theme" @click="changeTheme(theme)">
                            <button class="btn btn-ghost btn-sm w-full" :class="{
                                'text-accent': theme === currentTheme, // Add text-accent if selected
                            }">
                                {{ theme }}
                            </button>
                        </li>
                    </ul>
                </li>
                </li>
            </ul>
        </div>
    </header>
</template>

<script>
export default {
    data() {
        return {
            isMobileMenuOpen: false,
            themes: [
                "light",
                "dark",
                "cupcake",
                "bumblebee",
                "emerald",
                "corporate",
                "synthwave",
                "retro",
                "cyberpunk",
                "valentine",
                "halloween",
                "garden",
                "forest",
                "aqua",
                "lofi",
                "pastel",
                "fantasy",
                "wireframe",
                "black",
                "luxury",
                "dracula",
                "cmyk",
                "autumn",
                "business",
                "acid",
                "lemonade",
                "night",
                "coffee",
                "winter",
                "dim",
                "nord",
                "sunset",
            ],
            currentTheme: "light", // Default theme
        };
    },
    methods: {
        changeTheme(theme) {
            this.currentTheme = theme;
            document.documentElement.setAttribute("data-theme", theme);
        },
    },
    mounted() {
        // Set the initial theme (fallback to light if not stored in localStorage)
        const savedTheme = localStorage.getItem("theme") || "light";
        this.changeTheme(savedTheme);
    },
    watch: {
        currentTheme(newTheme) {
            // Save the theme to localStorage
            localStorage.setItem("theme", newTheme);
        },
    },
};
</script>
