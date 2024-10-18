<script>
    import * as Card from "$lib/components/ui/card/index.js";
    import { Textarea } from "$lib/components/ui/textarea";
    import { Button } from "$lib/components/ui/button";
    import Query from '$lib/components/query.svelte';
    import { threadStore } from "../../threadStore";
    import { goto } from '$app/navigation';
  
    let id;
    let title = '';
    let tags = [];
    let imageSrc;
    let postedBy;
    let timeAgo;
    let voteCount = 0;
    let description = '';

    let handlePost = () => {
        threadStore.update(prev => {
            let id = prev[prev.length - 1]?.id + 1 || 1;

            let storedTags = tags.map(tag => tag.id); 

            let newThread = {
                id: id,
                title, 
                description,
                tags: storedTags,
                imageSrc: `https://picsum.photos/1200/3200?random=1`,
                postedBy: "", 
                timeAgo: "0 hours",
                voteCount,
                comments: []
            };

            return [...prev, newThread];
        });

        goto(`/`);
    };
</script>

<div class="flex justify-center pt-8 px-4">
    <form class="w-full lg:w-2/3">
        <Card.Root>
            <Card.Title class="p-4 text-2xl">
                Let's help you post a new object!
            </Card.Title>

            <div class="p-4 pt-0">
                <Textarea bind:value={title} placeholder="First, we will start by titling it." />
            </div>

            <div class="p-4 pt-0">
                <Textarea bind:value={description} placeholder="Now let's give as much of a description as possible." />
            </div>

            <div class="p-4 pt-0 ">
                <Query bind:tags={tags} />
            </div>

            <div class="p-4 pt-0">
                <Button on:click={handlePost} variant="outline" size="icon" class="hover:bg-rose-900 flex items-center justify-center p-4 w-full text-lg">
                    Post
                </Button>
            </div>
        </Card.Root>
    </form>
</div>
