import { writable } from 'svelte/store';

export const threadStore = writable([
    {
        id: 1,
        title: "I found this in my grandmother's house, it's an old and very interesting object that I can't recognize, could someone help?",
        description: "I found this in my grandmother's house, it's an old and very interesting object that I can't recognize, could someone help?",
        imageSrc: `https://picsum.photos/1200/3200?random=1`,
        postedBy: "User123",
        timeAgo: "2 hours",
        voteCount: 150,
        comments: [
            {
                threadId: 1,
                commentId: 1,
                comment: "I think it's a very old object that was used in ancient times.I think it's a very old object that was used in ancient times.I think it's a very old object that was used in ancient times.I think it's a very old object that was used in ancient times.I think it's a very old object that was used in ancient times.I think it's a very old object that was used in ancient times.I think it's a very old object that was used in ancient times.I think it's a very old object that was used in ancient times.",
                voteCountComment: 10,
                commentator: "User456",
                timeAgoComment: "2 hours"
            },
            {
                threadId: 1,
                commentId: 2,
                comment: "It might be an antique tool used for farming.",
                voteCountComment: 15,
                commentator: "Historian101",
                timeAgoComment: "1 hour"
            },
            {
                threadId: 1,
                commentId: 3,
                comment: "It looks like something from the 19th century.",
                voteCountComment: 8,
                commentator: "ArtifactLover",
                timeAgoComment: "30 minutes"
            },
            {
                threadId: 1,
                commentId: 4,
                comment: "This could be a rare collectible from the Victorian era.This could be a rare collectible from the Victorian era.This could be a rare collectible from the Victorian era.This could be a rare collectible from the Victorian era.This could be a rare collectible from the Victorian era.This could be a rare collectible from the Victorian era.This could be a rare collectible from the Victorian era.This could be a rare collectible from the Victorian era.This could be a rare collectible from the Victorian era.This could be a rare collectible from the Victorian era.This could be a rare collectible from the Victorian era.",
                voteCountComment: 25,
                commentator: "CollectorGuru",
                timeAgoComment: "15 minutes"
            },            {
                threadId: 1,
                commentId: 1,
                comment: "I think it's a very old object that was used in ancient times.I think it's a very old object that was used in ancient times.I think it's a very old object that was used in ancient times.I think it's a very old object that was used in ancient times.I think it's a very old object that was used in ancient times.I think it's a very old object that was used in ancient times.I think it's a very old object that was used in ancient times.I think it's a very old object that was used in ancient times.",
                voteCountComment: 10,
                commentator: "User456",
                timeAgoComment: "2 hours"
            },
            {
                threadId: 1,
                commentId: 2,
                comment: "It might be an antique tool used for farming.",
                voteCountComment: 15,
                commentator: "Historian101",
                timeAgoComment: "1 hour"
            },
            {
                threadId: 1,
                commentId: 3,
                comment: "It looks like something from the 19th century.",
                voteCountComment: 8,
                commentator: "ArtifactLover",
                timeAgoComment: "30 minutes"
            },
            {
                threadId: 1,
                commentId: 4,
                comment: "This could be a rare collectible from the Victorian era.This could be a rare collectible from the Victorian era.This could be a rare collectible from the Victorian era.This could be a rare collectible from the Victorian era.This could be a rare collectible from the Victorian era.This could be a rare collectible from the Victorian era.This could be a rare collectible from the Victorian era.This could be a rare collectible from the Victorian era.This could be a rare collectible from the Victorian era.This could be a rare collectible from the Victorian era.This could be a rare collectible from the Victorian era.",
                voteCountComment: 25,
                commentator: "CollectorGuru",
                timeAgoComment: "15 minutes"
            },
            {
                threadId: 1,
                commentId: 5,
                comment: "I saw something similar in a museum exhibit last year.",
                voteCountComment: 18,
                commentator: "MuseumEnthusiast",
                timeAgoComment: "10 minutes"
            }
        ]
    },
    {
        id: 2,
        title: "Anyone knows what this is? It seems like something ancient and valuable!",
        description: "Anyone knows what this is? It seems like something ancient and valuable!",
        imageSrc: `https://picsum.photos/800/1200?random=2`,
        postedBy: "ChefMaster",
        timeAgo: "5 hours",
        voteCount: 95,
        comments: [
            {
                threadId: 2,
                commentId: 1,
                comment: "This looks like an old ceremonial item.",
                voteCountComment: 20,
                commentator: "User789",
                timeAgoComment: "3 hours"
            },
            {
                threadId: 2,
                commentId: 2,
                comment: "I have something similar in my collection!",
                voteCountComment: 12,
                commentator: "CollectorX",
                timeAgoComment: "2 hours"
            },
            {
                threadId: 2,
                commentId: 3,
                comment: "Looks like a rare artifact from ancient Egypt.",
                voteCountComment: 22,
                commentator: "Archaeologist101",
                timeAgoComment: "1 hour"
            },
            {
                threadId: 2,
                commentId: 4,
                comment: "It could be a tool used in ancient religious ceremonies.",
                voteCountComment: 9,
                commentator: "RelicHunter",
                timeAgoComment: "45 minutes"
            }
        ]
    },
    {
        id: 3,
        title: "Found this object in an antique shop, any ideas?",
        description: "Found this object in an antique shop, any ideas?",
        imageSrc: `https://picsum.photos/2000/1500?random=3`,
        postedBy: "ArtLover",
        timeAgo: "1 day",
        voteCount: 200,
        comments: [
            {
                threadId: 3,
                commentId: 1,
                comment: "It’s definitely an art piece from the early 1900s.",
                voteCountComment: 30,
                commentator: "VintageFan",
                timeAgoComment: "22 hours"
            },
            {
                threadId: 3,
                commentId: 2,
                comment: "Could be a limited edition artifact.",
                voteCountComment: 18,
                commentator: "RareFinds",
                timeAgoComment: "19 hours"
            },
            {
                threadId: 3,
                commentId: 3,
                comment: "This could have been part of a famous art collection.",
                voteCountComment: 25,
                commentator: "ArtCollector",
                timeAgoComment: "15 hours"
            },
            {
                threadId: 3,
                commentId: 4,
                comment: "I’ve seen similar items in antique fairs, very rare!",
                voteCountComment: 12,
                commentator: "AntiqueHunter",
                timeAgoComment: "10 hours"
            }
        ]
    },
    {
        id: 4,
        title: "This was handed down in my family, can anyone help identify it?",
        description: "This object has been in my family for generations, but no one knows what it is. Can anyone help?",
        imageSrc: `https://picsum.photos/1200/3200?random=4`,
        postedBy: "Historian101",
        timeAgo: "3 hours",
        voteCount: 175,
        comments: [] // No comments
    },
    {
        id: 5,
        title: "I bought this at a flea market, does anyone recognize it?",
        description: "I found this at a flea market. It looks really old. Can anyone tell me what it is?",
        imageSrc: `https://picsum.photos/800/1200?random=5`,
        postedBy: "BargainHunter",
        timeAgo: "6 hours",
        voteCount: 120,
        comments: [] // No comments
    },
    {
        id: 6,
        title: "Mystery object from my attic!",
        description: "This object was hidden in my attic for decades, does anyone know what it could be?",
        imageSrc: `https://picsum.photos/2000/1500?random=6`,
        postedBy: "ExplorerX",
        timeAgo: "12 hours",
        voteCount: 90,
        comments: [] // No comments
    },
    {
        id: 7,
        title: "Help me identify this unique artifact",
        description: "Found this unique artifact in an old box, not sure what it could be. Any guesses?",
        imageSrc: `https://picsum.photos/1000/1600?random=7`,
        postedBy: "CuriosityCollector",
        timeAgo: "1 day",
        voteCount: 210,
        comments: [] // No comments
    },
    {
        id: 8,
        title: "Does anyone know the origin of this item?",
        description: "I came across this item in my grandparent's storage. Can anyone tell me where it's from?",
        imageSrc: `https://picsum.photos/800/1200?random=8`,
        postedBy: "GenealogyBuff",
        timeAgo: "18 hours",
        voteCount: 145,
        comments: [] // No comments
    },
    {
        id: 9,
        title: "Ancient looking object found in a thrift store",
        description: "Picked up this ancient-looking object from a thrift store. Any ideas on what it could be?",
        imageSrc: `https://picsum.photos/1500/2200?random=9`,
        postedBy: "ThriftShopper",
        timeAgo: "3 hours",
        voteCount: 180,
        comments: [] // No comments
    },
    {
        id: 10,
        title: "Can someone help identify this mysterious relic?",
        description: "I found this mysterious relic at a local market. It looks quite old and unusual. Any thoughts?",
        imageSrc: `https://picsum.photos/800/1400?random=10`,
        postedBy: "MysteryFinder",
        timeAgo: "10 hours",
        voteCount: 110,
        comments: [] // No comments
    },
    {
        id: 11,
        title: "Interesting artifact passed down from my ancestors",
        description: "This artifact has been passed down for generations. It’s interesting but we have no clue about its origin.",
        imageSrc: `https://picsum.photos/1200/1600?random=11`,
        postedBy: "HeritageKeeper",
        timeAgo: "2 days",
        voteCount: 250,
        comments: [] // No comments
    },
    {
        id: 12,
        title: "Found this in a chest, any ideas?",
        description: "I opened an old chest in my basement and found this object inside. Any help identifying it?",
        imageSrc: `https://picsum.photos/1000/1300?random=12`,
        postedBy: "ChestOpener",
        timeAgo: "6 hours",
        voteCount: 135,
        comments: [] // No comments
    },
    {
        id: 13,
        title: "Does anyone know what this could be?",
        description: "This item was found among my great-grandparent’s belongings. Any experts out there who can identify it?",
        imageSrc: `https://picsum.photos/1600/2400?random=13`,
        postedBy: "FamilyHistorian",
        timeAgo: "4 hours",
        voteCount: 160,
        comments: [] // No comments
    }
]);
