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
    let postedDate;
    let voteCount = 0;
    let description = '';

    let handlePost = () => {
    const endPoint = 'http://localhost:8000/api/thread/';
    let data = new FormData();
    
    // Convert the tags array of objects to an array of IDs
    const tagIds = tags.map(tag => tag.id);
    
    data.append('title', title);
    data.append('tags', JSON.stringify(tagIds));  // Append only the tag IDs as a JSON string
    data.append('imageSrc', imageSrc);  // Ensure you're binding the file input to this
    data.append('postedBy', postedBy);
    data.append('voteCount', voteCount);
    data.append('description', description);

    fetch(endPoint, {
        method: 'POST',
        body: data
    }).then(response => {
        if (!response.ok) {
            return response.json().then(err => { throw new Error(JSON.stringify(err)); });
        }
        return response.json();
    })
    .then(data => {
        threadStore.update(prev => [...prev, data]);
        goto(`/`);
    })
    .catch(error => console.error('Error:', error));
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
            <input type="file" on:change={e => imageSrc = e.target.files[0]} />

            <div class="p-4 pt-0">
                <Button on:click={handlePost} variant="outline" size="icon" class="hover:bg-rose-900 flex items-center justify-center p-4 w-full text-lg">
                    Post
                </Button>
            </div>
        </Card.Root>
    </form>
</div>
