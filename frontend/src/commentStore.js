import { writable } from 'svelte/store';

export const commentStore = writable([
    {
        threadId: 1,
        commentId: 1,
        comment: "I think it's a very old object that was used in ancient times.",
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
        timeAgoComment: "1 hour 45 minutes"
    },
    {
        threadId: 2,
        commentId: 3,
        comment: "This looks like an old ceremonial item.",
        voteCountComment: 20,
        commentator: "User789",
        timeAgoComment: "4 hours 30 minutes"
    },
    {
        threadId: 2,
        commentId: 2,
        comment: "I have something similar in my collection!",
        voteCountComment: 12,
        commentator: "CollectorX",
        timeAgoComment: "4 hours"
    },
]);
