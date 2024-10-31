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
            const imageUrl = await uploadToSupabase(imageSrc);
            
            let data = new FormData();
            const tagIds = tags.map(tag => tag.id);
            data.append('title', title);
            data.append('tags', JSON.stringify(tagIds));
            data.append('imageSrc', imageUrl); 
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

<div class="flex justify-center p-4 lg:py-8 bg-change dark:bg-dark shifting">
    <form class="w-full lg:w-2/3">
        <Card.Root class="bg-opacity-90 hover:bg-opacity-100">
            <Card.Title class="p-4 text-2xl">
                Let's help you post new stuff!
            </Card.Title>

            <div class="p-4 pt-0">
                <Textarea class="min-h-10 h-10" bind:value={title} placeholder="First, we will start by titling it" />
            </div>

            <div class="p-4 pt-0">
                <Textarea 
                bind:value={description} 
                rows="10" 
                style="resize: vertical; white-space: pre-wrap;" 
                placeholder="To create a comprehensive visual description, please include as much detail as possible about the object. These might include, but are not limited to:
                
                • Material: Specify what the object is made of (e.g., wood, metal, plastic)
                • Size: Describe its dimensions or relative size
                • Shape: Note the overall form or geometry (e.g., round, square, irregular)
                • Color: Include main colors and any variations
                • Patterns and Textures: Describe any distinct patterns or surface textures
                • Weight: Mention if it's particularly heavy or light
                • Smell/Taste: If applicable, describe any notable smell or taste
                • Parts and Features: Outline any unique parts, images, icons, or symbols
                • Text and Language: Include any written elements and the language
                • Brand/Print: Mention any brands, prints, or logos
                • Functionality: Explain its purpose or how it’s typically used
                • Time Period: Specify any historical or cultural era it belongs to
                • Location: Mention where it’s typically found or originates from
                • Hardness: Describe if it’s soft, hard, or somewhere in between
                • Manmade or Natural: State if it's manufactured or naturally occurring"
            />
            </div>

            <div class="p-4 pt-0 ">
                <Query bind:tags={tags} />
            </div>

            <div class="p-4 pt-0">
                <Button
                    on:click={() => document.getElementById('file-input').click()}
                    variant="outline"
                    size="icon"
                    class="w-full flex items-center justify-center p-7 lg:p-4 text-center whitespace-normal break-words bg-black dark:bg-white text-white dark:text-black hover:bg-rose-900 hover:dark:bg-rose-900 transition-colors"
                    >
                    <span class="text-center">Let's upload an image of your object to wrap it up</span>
                </Button>
                <input id="file-input" type="file" on:change={e => imageSrc = e.target.files[0]} class="hidden" />
              </div>
              
              <div class="p-4 pt-0">
                <Button
                    on:click={handlePost}
                    variant="outline"
                    size="icon"
                    class="hover:bg-rose-900 hover:dark:bg-rose-900 p-7 lg:p-4 w-full bg-black dark:bg-white text-white dark:text-black transition-colors flex items-center justify-center text-center whitespace-normal break-words"
                    >
                    Check your details, and when you're ready, click here to post it!
              </Button>
              </div> 

        </Card.Root>
    </form>
</div>
