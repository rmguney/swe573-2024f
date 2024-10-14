<script>
    import "../app.css";
    import PostContainer from '$lib/components/postContainer.svelte';
    import Explore from '$lib/components/explore.svelte';
    import Leaderboard from '$lib/components/leaderboard.svelte';
</script>

<div class="fixed overflow-hidden w-full ">

    <div class="flex flex-row h-full min-h-screen text-text justfiy-between bg-none">
        <Explore class="" />
        
        <div class="flex-grow overflow-auto">
            <PostContainer class="" />
        </div>

        <Leaderboard class="hidden lg:block" />
    </div>

</div>
