import { writable } from 'svelte/store';

export const threadStore = writable([
    {
        id: 1,
        title: "I found this in my grandmother's house, it's an old and very interesting object that I can't recognize, could someone help?",
        description: "I found this in my grandmother's house, it's an old and very interesting object that I can't recognize, could someone help?",
        tags: ["Q16338", "Q204370", "Q185157"],
        imageSrc: `https://picsum.photos/1200/3200?random=1`,
        postedBy: "User123",
        postedDate: "22 hours",
        voteCount: 150,
        comments: [
            {
                commentId: 1,
                comment: "I think it's a very old object that was used in ancient times.",
                voteCountComment: 10,
                commentator: "User456",
                postedDateComment: "2 hours"
            },
            {
                commentId: 2,
                comment: "It might be an antique tool used for farming.",
                voteCountComment: 15,
                commentator: "Historian101",
                postedDateComment: "1 hour 45 minutes"
            }
        ]
    },
    {
        id: 2,
        title: "Anyone knows what this is? It seems like something ancient and valuable!",
        description: "Anyone knows what this is? It seems like something ancient and valuable!",
        tags: ["Q340", "Q102866", "Q309"],
        imageSrc: `https://picsum.photos/800/1200?random=2`,
        postedBy: "ChefMaster",
        postedDate: "22 hours",
        voteCount: 95,
        comments: [
            {
                commentId: 1,
                comment: "This looks like an old ceremonial item.",
                voteCountComment: 20,
                commentator: "User789",
                postedDateComment: "4 hours 30 minutes"
            },
            {
                commentId: 2,
                comment: "I have something similar in my collection!",
                voteCountComment: 12,
                commentator: "CollectorX",
                postedDateComment: "4 hours"
            }
        ]
    },
    {
        id: 3,
        title: "Found this object in an antique shop, any ideas?",
        description: "Found this object in an antique shop, any ideas?",
        tags: ["Q280528", "Q7388", "Q220584"],
        imageSrc: `https://picsum.photos/2000/1500?random=3`,
        postedBy: "ArtLover",
        postedDate: "21 hours",
        voteCount: 200,
        comments: [
            {
                commentId: 1,
                comment: "It’s definitely an art piece from the early 1900s.",
                voteCountComment: 30,
                commentator: "VintageFan",
                postedDateComment: "22 hours"
            }
        ]
    },
    {
        id: 4,
        title: "This was handed down in my family, can anyone help identify it?",
        description: "This object has been in my family for generations, but no one knows what it is. Can anyone help?",
        tags: ["Q106407", "Q3533467"],
        imageSrc: `https://picsum.photos/1200/3200?random=4`,
        postedBy: "Historian101",
        postedDate: "18 hours",
        voteCount: 175,
        comments: []
    },
    {
        id: 5,
        title: "I bought this at a flea market, does anyone recognize it?",
        description: "I found this at a flea market. It looks really old. Can anyone tell me what it is?",
        tags: ["Q205818", "Q9136", "Q55678"],
        imageSrc: `https://picsum.photos/800/1200?random=5`,
        postedBy: "BargainHunter",
        postedDate: "16 hours",
        voteCount: 120,
        comments: []
    },
    {
        id: 6,
        title: "Mystery object from my attic!",
        description: "This object was hidden in my attic for decades, does anyone know what it could be?",
        tags: ["Q223808", "Q204425"],
        imageSrc: `https://picsum.photos/2000/1500?random=6`,
        postedBy: "ExplorerX",
        postedDate: "12 hours",
        voteCount: 90,
        comments: []
    },
    {
        id: 7,
        title: "Help me identify this unique artifact",
        description: "Found this unique artifact in an old box, not sure what it could be. Any guesses?",
        tags: ["Q83077", "Q174424"],
        imageSrc: `https://picsum.photos/1000/1600?random=7`,
        postedBy: "CuriosityCollector",
        postedDate: "12 hours",
        voteCount: 210,
        comments: []
    },
    {
        id: 8,
        title: "Does anyone know the origin of this item?",
        description: "I came across this item in my grandparent's storage. Can anyone tell me where it's from?",
        tags: ["Q222323", "Q619272"],
        imageSrc: `https://picsum.photos/800/1200?random=8`,
        postedBy: "GenealogyBuff",
        postedDate: "11 hours",
        voteCount: 145,
        comments: []
    },
    {
        id: 9,
        title: "Ancient looking object found in a thrift store",
        description: "Picked up this ancient-looking object from a thrift store. Any ideas on what it could be?",
        tags: ["Q15381", "Q6256", "Q23787"],
        imageSrc: `https://picsum.photos/1500/2200?random=9`,
        postedBy: "ThriftShopper",
        postedDate: "8 hours",
        voteCount: 180,
        comments: []
    }
]);
