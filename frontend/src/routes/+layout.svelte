<script lang="ts">
	import '@/styles/main.scss';
</script>

<div>
	<div class="box-border flex flex-col items-center justify-center">
		<p class="text-3xl font-bold">Any element could go here, I am shown for all children routes</p>
	</div>
	<main>
		<slot />
	</main>
</div>

<style lang="scss">
</style>
