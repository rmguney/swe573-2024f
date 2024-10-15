<script>
    import "../app.css";
    import PostContainer from '$lib/components/postContainer.svelte';
    import Explore from '$lib/components/explore.svelte';
    import Leaderboard from '$lib/components/leaderboard.svelte';
</script>

<div class="w-full">

    <div class="flex flex-row h-full min-h-screen text-text justfiy-between bg-gradient-to-br from-[#c08081] to-[#49796b]">
        <Explore />
        <div class="flex-grow overflow-auto ">
            <PostContainer , />
        </div>
        <Leaderboard />
    </div>
</div>