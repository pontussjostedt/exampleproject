<script lang="ts">
	let inputContent = '';
	let tasks: string[] = [];
	const onclick = () => {
		//called everytime we press the add button
		tasks.push(inputContent);
		console.log(tasks);
	};
</script>

<div class="flex h-screen flex-col items-center justify-center">
	<p>text</p>
	<div class="grid-rows-2">
		<input class="border-2 border-pink-400" bind:value={inputContent} />
		<button class="bg-pink-400" on:click={onclick}>Add</button>
	</div>
</div>

<style lang="scss">
</style>
