<script>
    import * as Card from "$lib/components/ui/card/index.js";
    import { Textarea } from "$lib/components/ui/textarea";
    import { Button } from "$lib/components/ui/button";
    import Query from '$lib/components/query.svelte';
    import { threadStore } from "../../threadStore";
    import { goto } from '$app/navigation';
    import { activeUser } from '../../userStore';

    let title = '';
    let tags = [];
    let imageSrc; 
    let postedBy;
    let voteCount = 0;
    let description = '';

    $: postedBy = $activeUser;

    const uploadToSupabase = async (file) => {
    const supabaseUrl = import.meta.env.VITE_SUPABASE_URL;
    const anonKey = import.meta.env.VITE_SUPABASE_ANON_KEY;
    const bucketName = "threef_bucket";
    const fileName = file.name;

    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch(`${supabaseUrl}/storage/v1/object/${bucketName}/${fileName}`, {
        method: "POST",
        headers: {
            "apikey": anonKey,
            "Authorization": `Bearer ${anonKey}`
        },
        body: formData
    });

    if (!response.ok) {
        const errorDetails = await response.json();
        console.error("Supabase upload error details:", errorDetails);
        throw new Error("Failed to upload image to Supabase");
    }

    return `${supabaseUrl}/storage/v1/object/public/${bucketName}/${fileName}`;
};

    let handlePost = async () => {
        const endPoint = 'https://threef.vercel.app/api/thread/';
        
        try {
            // Upload image to Supabase first
            const imageUrl = await uploadToSupabase(imageSrc);
            
            // Prepare data for backend API request
            let data = new FormData();
            const tagIds = tags.map(tag => tag.id);
            data.append('title', title);
            data.append('tags', JSON.stringify(tagIds));
            data.append('imageSrc', imageUrl);  // Use the URL instead of the file
            data.append('postedBy', postedBy); 
            data.append('voteCount', voteCount);
            data.append('description', description);

            const response = await fetch(endPoint, {
                method: 'POST',
                body: data
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(JSON.stringify(errorData));
            }

            const responseData = await response.json();
            threadStore.update(prev => [...prev, responseData]);
            goto(`/`);
        } catch (error) {
            console.error('Error:', error);
        }
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
            
            <!-- File input for image -->
            <input type="file" on:change={e => imageSrc = e.target.files[0]} />

            <div class="p-4 pt-0">
                <Button on:click={handlePost} variant="outline" size="icon" class="hover:bg-rose-900 flex items-center justify-center p-4 w-full text-lg">
                    Post
                </Button>
            </div>
        </Card.Root>
    </form>
</div>
