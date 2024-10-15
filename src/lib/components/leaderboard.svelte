<script>
    import * as Card from "$lib/components/ui/card";

    let topContributors = [
    { name: "User123", contributions: 120 },
    { name: "ChefMaster", contributions: 110 },
    { name: "ArtLover", contributions: 110 },
    { name: "TechieGuy", contributions: 105 },
    { name: "TravelerX", contributions: 100 },
    { name: "MusicManiac", contributions: 95 },
    { name: "ScienceGeek", contributions: 90 },
    { name: "HistoryBuff", contributions: 85 },
    { name: "Fashionista", contributions: 80 },
    { name: "FitnessFreak", contributions: 75 }
];

</script>

<div class="hidden lg:block pr-8 pt-8 text-center">
    <Card.Root class="w-56">
        <Card.Header>
            <Card.Title class="pb-2">Top Contributors</Card.Title>
        </Card.Header>

                {#each topContributors as contributor}
                <Card.Description class="px-6 py-3">
                    {contributor.name} 
                    <br>
                    {contributor.contributions} points        
                </Card.Description>
                {/each}

    </Card.Root>
</div>
