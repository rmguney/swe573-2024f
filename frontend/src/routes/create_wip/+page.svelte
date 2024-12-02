<script>
    import * as Card from "$lib/components/ui/card/index.js";
    import { Textarea } from "$lib/components/ui/textarea";
    import { Button } from "$lib/components/ui/button";
    import Query from '$lib/components/query.svelte';
    import { threadStore } from "../../threadStore";
    import { goto } from '$app/navigation';
    import { activeUser } from '../../userStore';

    let title = '';
    let tags = []; // Tags will include detailed info after fetching
    let imageSrc; 
    let postedBy;
    let description = '';
    let material = '';
    let size = '';
    let shape = '';
    let color = '';
    let texture = '';
    let weight = '';
    let smell = '';
    let marking = '';
    let functionality = '';
    let period = '';
    let location = '';
    let anonymous = false; 
    let resolved = false;

    $: postedBy = $activeUser;

    function generateRandomString(length) {
        const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
        let result = '';
        for (let i = 0; i < length; i++) {
            result += characters.charAt(Math.floor(Math.random() * characters.length));
        }
        return result;
    }

    const uploadToSupabase = async (file) => {
        const supabaseUrl = import.meta.env.VITE_SUPABASE_URL;
        const anonKey = import.meta.env.VITE_SUPABASE_ANON_KEY;
        const bucketName = "threef_bucket";
        const fileExtension = file.name.split('.').pop();
        const fileName = `${generateRandomString(5)}.${fileExtension}`;

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

    const fetchTagDetails = async (tagIds) => {
        const details = [];
        for (const id of tagIds) {
            const response = await fetch(`https://www.wikidata.org/wiki/Special:EntityData/${id}.json`);
            if (response.ok) {
                const data = await response.json();
                const entity = data.entities[id];
                details.push({
                    id,
                    title: entity.labels?.en?.value || "Unknown",
                    description: entity.descriptions?.en?.value || "No description available"
                });
            } else {
                console.error(`Failed to fetch data for tag ID: ${id}`);
            }
        }
        return details;
    };

    const handlePost = async () => {
        const endPoint = 'https://threef.vercel.app/api/thread/';

        try {
            // Fetch titles and descriptions for the tags
            const detailedTags = await fetchTagDetails(tags.map(tag => tag.id));
            
            const imageUrl = await uploadToSupabase(imageSrc);
            
            let data = new FormData();
            data.append('title', title);
            data.append('tags', JSON.stringify(detailedTags)); // Send detailed tags
            data.append('imageSrc', imageUrl); 
            data.append('postedBy', anonymous ? 'Anonymous' : postedBy);
            data.append('description', description);
            data.append('material', material);
            data.append('size', size);
            data.append('shape', shape);
            data.append('color', color);
            data.append('texture', texture);
            data.append('weight', weight);
            data.append('smell', smell);
            data.append('marking', marking);
            data.append('functionality', functionality);
            data.append('period', period);
            data.append('location', location);
            data.append('resolved', resolved);

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

<div class="flex justify-center p-4 lg:py-8 bg-change dark:bg-dark shifting">
    <form class="w-full lg:w-2/3">
        <Card.Root class="bg-opacity-90 hover:bg-opacity-100">
            <Card.Title class="p-4 text-2xl">
                Let's help you post new stuff!
            </Card.Title>

            <div class="p-4 pt-2">
                <Textarea class="min-h-10 h-10" bind:value={title} placeholder="First, we will start by titling it. This is what people will see on their homepage so try to make it interesting" />
            </div>

            <div class="p-4 pt-0">
                <Textarea 
                bind:value={material} 
                placeholder="What is the object made of? (e.g. wood, metal, etc.)"
                class="min-h-10 h-10" />
            </div>
            
            <div class="p-4 pt-0">
                <Textarea 
                bind:value={size} 
                style="resize: vertical; white-space: pre-wrap;" 
                placeholder="What are the dimensions? (e.g. 10cm x 5cm x 3cm)"
                class="min-h-10 h-10" />
            </div>
            
            <div class="p-4 pt-0">
                <Textarea 
                bind:value={shape} 
                style="resize: vertical; white-space: pre-wrap;" 
                placeholder="What is the shape? (e.g. round, square, etc.)"
                class="min-h-10 h-10" />
            </div>
            
            <div class="p-4 pt-0">
                <Textarea 
                bind:value={color} 
                style="resize: vertical; white-space: pre-wrap;" 
                placeholder="What is the color? (e.g. red, blue, etc.)"
                class="min-h-10 h-10" />
            </div>
            
            <div class="p-4 pt-0">
                <Textarea 
                bind:value={texture} 
                style="resize: vertical; white-space: pre-wrap;" 
                placeholder="What is the texture? (e.g. smooth, rough, etc.)"
                class="min-h-10 h-10" />
            </div>
            
            <div class="p-4 pt-0">
                <Textarea 
                bind:value={weight} 
                style="resize: vertical; white-space: pre-wrap;" 
                placeholder="What is the weight? (e.g. 100g, 1kg, etc.)"
                class="min-h-10 h-10" />
            </div>
            
            <div class="p-4 pt-0">
                <Textarea 
                bind:value={smell} 
                style="resize: vertical; white-space: pre-wrap;" 
                placeholder="What is the smell? (e.g. sweet, sour, etc.)"
                class="min-h-10 h-10" />
            </div>
            
            <div class="p-4 pt-0">
                <Textarea 
                bind:value={marking} 
                style="resize: vertical; white-space: pre-wrap;" 
                placeholder="What are the markings? (e.g. logo, text, etc.)"
                class="min-h-10 h-10" />
            </div>
            
            <div class="p-4 pt-0">
                <Textarea 
                bind:value={functionality} 
                style="resize: vertical; white-space: pre-wrap;" 
                placeholder="What is the functionality? (e.g. cutting, writing, etc. or maybe it does something unique)"
                class="min-h-10 h-10" />
            </div>
            
            <div class="p-4 pt-0">
                <Textarea 
                bind:value={period} 
                style="resize: vertical; white-space: pre-wrap;" 
                placeholder="What is the period? (e.g. 1800s, 1900s, etc.)"
                class="min-h-10 h-10" />
            </div>
            
            <div class="p-4 pt-0">
                <Textarea 
                bind:value={location} 
                style="resize: vertical; white-space: pre-wrap;" 
                placeholder="Where is it typically found? (e.g. Europe, Asia, etc. or you can be more precise if you can.)"
                class="min-h-10 h-10" />
            </div>            

            <div class="p-4 pt-0">
                <Textarea 
                bind:value={description} 
                style="resize: vertical; white-space: pre-wrap;" 
                placeholder="Then maybe some additional description about the object you're posting."
                class="min-h-10 h-10" />
            </div>

            <div class="p-4 pt-0">
                <Query bind:tags={tags} />
            </div>

            <div class="p-4 pt-2">
                <input type="checkbox" bind:checked={anonymous} id="anonymous-checkbox" />
                <label for="anonymous-checkbox" class="ml-2">If you wish you can check this box to post anonymously, otherwise you may leave it unchecked</label>
            </div>

            <div class="p-4 pt-0">
                <Button
                    on:click={() => document.getElementById('file-input').click()}
                    variant="outline"
                    size="icon"
                    class="w-full flex items-center justify-center p-7 lg:p-4 text-center whitespace-normal break-words bg-black dark:bg-white text-white dark:text-black hover:text-white hover:bg-rose-900 hover:dark:bg-rose-900 transition-colors"
                    >
                    <span class="text-center">Lastly, let us upload an image or a video of your object to wrap it up</span>
                </Button>
                <input id="file-input" type="file" on:change={e => imageSrc = e.target.files[0]} class="hidden" />
            </div>

            <div class="p-4 pt-0">
                <Button
                    on:click={handlePost}
                    variant="outline"
                    size="icon"
                    class="hover:bg-rose-900 hover:dark:bg-rose-900 p-7 lg:p-4 w-full bg-black dark:bg-white text-white dark:text-black hover:text-white transition-colors flex items-center justify-center text-center whitespace-normal break-words"
                    >
                    Check your details, and when you're ready, click here to post it!
              </Button>
            </div> 

        </Card.Root>
    </form>
</div>
