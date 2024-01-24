<script lang="ts">
	import config from "@/public-config"
	import { onMount } from "svelte";
	import type { PageData } from "./$types";

	let inputContent = '';
	let tasks: string[] = [];

	const onclick = async () => {
		if(inputContent.length > 0){
			await fetch(`${config.API_URL}/addmessage?message=${inputContent}`, {headers: {Origin: "http://localhost:3000"}}) //bad practice to hardcode in url string
			tasks = [...tasks, inputContent]; // need to reasign tasks for svelte to update foreach block
		}
	};

	export let data: PageData

	onMount(() => {
		tasks = data.messages
	})
</script>

<div class="flex h-screen flex-col items-center justify-items-center">
	<p>text</p>
	<div class="grid-rows-2">
		<input class="border-2 border-pink-400" bind:value={inputContent} />
		<button class="bg-pink-400" on:click={onclick}>Add</button>
	</div>
	<div class="flex flex-col">
		{#each tasks as task}
			<h1>{task}</h1>
		{/each}
	</div>
</div>

<style lang="scss">
</style>
