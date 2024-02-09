const t1 = "Once is necessary twice is preferable. Taking notes is also a good idea and will help the writing process by making it easy to refer to your in-the-moment thoughts and reactions.";
const t2 = "Are you writing for a fan site, a national news outlet, or a Teen Magazine? Knowing who your readers are can help you decide what elements of the movie to highlight. You should also adjust your writing style to fit the target audience.";
const t3 = "Professional reviewers do not shy away from telling their readers whether they thought the movie was good, bad, or indifferent; in fact, readers come to rely on those reviewers whose tastes reflect their own when deciding whether or not to spend their time and money. Professional reviewers also have watched a lot of movies and can express why and how they came to their criticism. Be sure to back up your thoughts with specifics–a disappointing performance, a ridiculous plot, beautiful cinematography, difficult material that leaves you thinking, and so on.";
const t4 = "The best reviewers have a distinct personality that comes across in their writing. This does not happen overnight, so take every opportunity to write as an opportunity to develop your own style and voice that will grab reader’s attention and keep them coming back for more.";
const t5 = "As with all writing endeavors, the more you read the better you will be. And when you read film reviews that you like (or don’t like), think about why. Use your critical eye to think about why one reviewer has a hundred thousand followers and another only has two. Be sure also to read the publications where you’d like your writing to appear as a template for your own reviews, and don’t forget to read the submission guidelines!";
const t6 = "Give your readers some idea of the plot, but be careful not to include any spoilers. Remember the point of a good review is to get people interested in going to the movie. Don’t get over excited and ruin it for them!";
const t7 = "Many casual filmgoers will be inspired to see a movie if a favorite actor is in it, so you should probably spend a little space talking about the performances: seasoned actor in a new kind of role, brilliant performance from a rising star, excellence despite a lackluster script, dynamics in an ensemble, and so much more can be said about the actors in any given film.";
const t8 = "This is where your film geek can really shine. Tell your readers about the highlights or missteps of directors, cinematographers, costume designers and CGI magicians. What worked, what surprised, what fell short of expectations, are all great questions to address in the body of your review.";
const t9 = "Edit your work; your opinions will not be taken seriously if you misspell the director’s name or can’t put together a grammatically correct sentence. Take the time to check your spelling and edit your piece for organizational flow.";


let text_array = [];

text_array.push(t1, t2, t3, t4, t5, t6, t7, t8, t9);

text_array.sort(function (firstEl, secondEl) {
    if (firstEl.length <= secondEl.length) {
        return -1;
    } else return 0;
});
for (let i = 0; i < text_array.length; ++i) {
    if (i == 0) {
        document.getElementById("one").innerText = text_array[i];
    }
    if (i == 1) {
        document.getElementById("two").innerText = text_array[i];
    }
    if (i == 2) {
        document.getElementById("three").innerText = text_array[i];
    }
    if (i == 3) {
        document.getElementById("four").innerText = text_array[i];
    }
    if (i == 4) {
        document.getElementById("five").innerText = text_array[i];
    }
    if (i == 5) {
        document.getElementById("six").innerText = text_array[i];
    }
    if (i == 6) {
        document.getElementById("seven").innerText = text_array[i];
    }
    if (i == 7) {
        document.getElementById("eight").innerText = text_array[i];
    }
    if (i == 8) {
        document.getElementById("nine").innerText = text_array[i];
    }
}
