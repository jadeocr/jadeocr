<template>
	<div class='container mx-auto text-base text-2xl sm:text-3xl md:text-4xl lg:text-5xl xl:text-6xl
	mt-24 sm:mt-32 md:mt-40 lg:mt-56 xl:mt-64'>
    <p>囧</p>
    <p>404 Not Found</p>
    <router-link :to='{ name: "landing" }'
    class='bg-purple-500 hover:bg-purple-600 mt-8 px-3 py-1 
    text-base sm:text-xl md:text-2xl lg:text-3xl xl:text-4xl rounded-lg'
    >
      Home | 返回
    </router-link>
	</div>
</template>

<script>
export default {

}
</script>

<style scoped>
.container{
	text-align: center;
}
</style>