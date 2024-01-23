<script lang="ts">
	let inputContent = '';
	let tasks: string[] = [];

	const onclick = () => {
		//called everytime we press the add button
		tasks = [...tasks, inputContent]; // need to reasign tasks for svelte to update foreach block
	};
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
