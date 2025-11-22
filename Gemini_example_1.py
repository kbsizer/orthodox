#!/usr/bin/env python
"""
Using the google-genai Python Library

google-genai features:

    Unified Interface: It provides a single, consistent interface for working with all of Google's state-of-the-art
    generative models (like Gemini) and is designed to simplify the process of building GenAI applications.

    Ease of Use: As you saw in the script, it abstracts away the need to manually construct HTTP requests (like you
    would with the raw REST API), handle JSON serialization, and manage lower-level network details.

    Automatic Authentication: It automatically detects and uses the GEMINI_API_KEY environment variable, making
    credential management clean and secure.

    Future-Proof: It's the SDK that will receive the latest feature updates, including support for streaming,
    function calling, multimodal inputs (images and video), and advanced configuration.


You can easily read the entire contents of a large text file (up to 50MB using the Files API, or up to 4 million
characters by reading it into a string) and include it directly in your Python script's prompt string without
hitting the limit.

Example of the Prompt Structure
The full content of your file just becomes part of the prompt string:

Note: The prompt size limit includes all text you send: your instructions, the file content, and any metadata.
However, with 1 million tokens, you generally don't need to worry about this unless you are submitting an
extremely large corpus of data.

Alternative: Using the Files API for Large Files
While your 50,000-character files work fine in the contents string, if you ever deal with files larger than 10MB
or want to upload non-text formats (like PDFs or images), the Files API is the more robust approach.

The Files API allows you to upload the file once and reference it by a file ID in your prompt, which is more
efficient for very large or complex inputs.

Token vs. Character
Since you deal with characters, here is the approximate conversion:1 Token is approximately 4 characters in English.
The 1,000,000 token limit translates to a maximum prompt size of roughly 4 million characters
(or about 10,000 single-spaced pages of text).

Example: Suppose you have a 50,000-character file
Approximate Tokens: (50,000 characters) / (4 characters/token) = 12,500 tokens
Comparing this to the model's limit:
Your Tokens (12,500) vs. Model's Limit (1,000,000)
Your files are only using about 1.25% of the model's total capacity.
You could easily submit documents that are 80 times longer.

HOW TO OBTAIN A GEMINI API KEY
1) Go to Google AI Studio:
    Open your web browser and navigate to the official Google AI Studio website:
    https://aistudio.google.com/

2) Sign in with your Google Account.

3) Navigate to API Key Creation:
    Once you are logged in, look for the "Get API key" button. This is often found prominently
    on the lower left of the main page or in the left-hand navigation menu (Dashboard).

4) Create a New API Key:
    On the API Keys page, click the "Create API key" button.
    The system will prompt you to select a Google Cloud Project to associate the key with.
    For new users, a default project is often created automatically. If you have multiple projects,
    choose the one you want to use for your API access.

5) Copy and Secure Your Key:
    Once you click "Create key," your new API key (a long string of characters) will be generated and displayed.
    Copy this key immediately! For security reasons, you will not be able to view the full key again once you
    leave this page.

    Store it securely, as it's the credential that links API usage to your account (and any associated billing).

6) How to Use the Key in Your Python Script
    After copying the key, the best practice (as used in the script before) is to set it as an environment
    variable named GEMINI_API_KEY.

    Set the Environment Variable:

            export GEMINI_API_KEY="YOUR_API_KEY_HERE"
"""

import os
from google import genai
from google.genai.types import FinishReason


def main():

    # The entire file content (up to 4 million characters) is here
    file_content = """
    TO THE MAKARYGIN FAMILY Nara and her Innokenty had been far-off,
    disembodied relatives until a year ago. They had flitted through Moscow for
    one short week in a year and sent presents at holiday times. Klara, who had got
    used to calling Galakhov, her famous older brother-in-law, Kolya, was still
    shy and tongue-tied with Innokenty.
    But last summer they had stayed longer, and Nara was often at her parents’
    apartment, usually complaining about her husband and the shadow over their
    marriage, which until recently had been so happy. She and Alevtina
    Nikanorovna discussed it at length, and if she happened to be at home, Klara
    listened, openly or surreptitiously. She could not have refrained even if she had
    wanted to. This was, after all, life’s greatest mystery: What made people love
    each other or not love each other?
    Her sister told them about all sorts of trivial incidents, disagreements,
    quarrels, suspicions, and also about Innokenty’s professional misjudgments; he
    had changed so much, he showed no respect for the opinions of important
    people, and this affected their material position so that Nara had to go without
    things. As she told it, Nara was always right, her husband always wrong.
    Klara, privately, drew quite different conclusions. Nara did not know how
    lucky she was. She probably no longer loved Innokenty but only herself. What
    she cared about was not his work but the status it gave her, not his views and
    preferences, however they might have changed, but her possession of him,
    asserted for all to see. Klara was surprised to find that her sister resented her
    husband’s suspected infidelities less than his failure to emphasize sufficiently
    in the presence of other women that she alone was supremely important to him.
    The unmarried younger sister could not help comparing her own situation
    with Nara’s and telling herself that, come what may, she would have behaved
    differently. How could Nara be satisfied with anything that left him unhappy?
    Their problem was aggravated by their childlessness.
    Once Klara had opened her heart on the stairway, they were on such easy
    terms that she urgently needed to see more of him. She had such a backlog of
    questions that Innokenty was just the man to answer!
    But the presence of Nara or any other member of the family would somehow
    make it awkward.
    So when Innokenty suggested, shortly afterward, a day out in the country, her
    heart missed a beat and she agreed without thinking.
    “No manor houses, museums, or famous ruins, though,” Innokenty said with a
    faint smile.
    “I don’t like them either” was Klara’s firm response.
    Now that she knew some of his troubles, his halfhearted smile caused a
    twinge of sympathy.
    “Switzerland and places like that can drive a man crazy,” he said.
    “Wandering around ordinary Russian countryside is good enough for me. Think
    we can find any?”
    Klara nodded vigorously. “We can if we try!”
    It was left unclear whether this was to be an outing for two or for three. But
    Innokenty arranged to meet her on a weekday at the Kiev Station. He did not
    phone his home and would not call for Klara at Kaluga Gate, which made it
    obvious that there would be just the two of them and that Klara’s parents were
    probably not supposed to know.
    As far as her sister was concerned, Klara felt quite entitled to this outing.
    Even if his marriage had been perfect, Innokenty would have been just paying
    his family dues. As things were, Nara had only herself to blame.
    Would there ever again be such a wonderful day in Klara’s life? There
    would certainly be none for which preparations were so agonizing. What
    should she wear? If her women friends could be believed, no color suited her,
    but she had to choose one of them! She put on a brown dress and carried a blue
    coat. Her veil gave her more trouble than anything; the night before, she spent
    two hours trying it on, taking it off, trying it on again. Some lucky people can
    make their minds up at once! Klara was crazy about veils; especially in films,
    they made a woman enigmatic, raised her beyond the reach of critical scrutiny.
    Still, she decided against it. Innokenty had grown tired of French frippery, and,
    besides, it was going to be a sunny day. She did put on her black net gloves,
    though. Black net gloves were very pretty.
    The Maloyaroslav train was waiting when they arrived. A small steam
    locomotive, it was splendid. They had no particular station in mind. They
    simply took tickets to the end of the line. The route was so new to them that
    they were both startled when fellow passengers mentioned a station called
    “Nara.” If Innokenty had known about it, he might perhaps have chosen a
    different terminus. If Klara had ever known, she had completely forgotten.
    “Nara, Nara, Nara. . . .” They heard the name over and over again in the
    course of the journey. It seemed to haunt them.
    It was a cool morning for August. They were both cheerful and animated, and
    they were soon chatting freely about anything and everything. Occasional
    lapses into formality ended in laughter and made them feel even more at ease.
    Innokenty was wearing some sort of Western sports outfit, unconcernedly
    creasing and rumpling what he evidently thought of as “casual clothes.”
    They had the whole day ahead of them, but Klara began eagerly interrogating
    him, switching erratically from questions about Europe to problematic aspects
    of Soviet life. She wasn’t quite sure herself what she wanted to know! But she
    knew there was something! She longed to be cleverer! She had to get to the
    bottom of it!
    Innokenty wagged his head comically.
    “Do you really think . . . little Klara . . . that I understand any of it myself?”
    “But you diplomats are there to show the rest of us the way, and now you tell
    me you don’t understand.”
    “Ah, but all my colleagues do understand; it’s only I who don’t. And even I
    understood it all till some time last year or the year before last.”
    “Then what happened?”
    “Do you know, that’s another thing I don’t understand,” Innokenty said
    laughingly. “And anyway, my little Klara, who knows where the explanation
    should start? It goes back to the very beginning of things. Suppose a caveman
    suddenly popped out from under the seat here and asked us to explain in not
    more than five minutes how trains can run on electricity. What would we tell
    him? First of all, off you go and learn to read. Then get on with your arithmetic,
    algebra, draftsmanship, electrotechnology. . . . Have I forgotten anything?”
    “I don’t know . . . magnetics, perhaps?”
    “There you are, you don’t know either. And you’re in your final year! Then I
    would say, ‘Come back in fifteen years’ time, and I’ll explain it in five minutes,
    only by then you’ll know it all yourself.’ ”
    “Very well, I’m willing to learn. But how do I go about it? Where do I
    begin?”
    “Well, our newspapers will do for a start.”
    A man with a leather satchel was passing through the train selling
    newspapers. Innokenty bought Pravda from him.
    Klara had realized when they boarded the train that they would be having a
    rather special conversation, and she had sent Innokenty ahead to occupy an
    uncomfortable double seat by a door. Innokenty hadn’t understood, but only
    there could they talk more or less freely.
    “All right, now for our reading lesson,” he said, unfolding the paper. “Take
    this headline: ‘Women Filled with Labor Enthusiasm Overfulfill Norms.’ Ask
    yourself why they have to think about norms at all. Don’t they have anything to
    do at home? What it means is that the combined wages of husband and wife
    aren’t enough to support a family. Whereas the husband’s wage alone ought to
    be enough.”
    “Is it enough in France?”
    “And everywhere else. Look, here’s another bit: ‘In all the capitalist
    countries together there are fewer day nurseries than in our country.’ True?
    Probably. But one little detail is left out: In all other countries women are freer
    to bring up their children themselves, so they don’t need all these nurseries.”
    The train shuddered. They were moving.
    Innokenty found another text without difficulty, pointed to it, and spoke into
    her ear through the racket.
    “Now take any apparently insignificant form of words: ‘Member of the
    French parliament so-and-so made a statement’ . . . about the hatred of the
    French people for the Americans. Did he, you ask? He probably did; we only
    print the truth! But something is left out. What party does he belong to? If he
    were not a Communist, they would certainly say so because it would make his
    utterance all the more valuable! So he is a Communist. But they don’t say so!
    And that’s the way it always is, Clairette. They’ll write about record snowfall
    somewhere, with thousands of cars buried in drifts—a national disaster! But
    the artful implication is that where there are so many cars, it isn’t worth
    building garages for them. These are all examples of freedom from
    information! The same sort of thing turns up in the sports pages: ‘match ended
    in well-deserved victory’—no need to read on, obviously our side won. But if
    ‘to the surprise of the spectators the jury declared so-and-so the winner,’soand-so
    is obviously not one of ours.”
    Innokenty looked around for somewhere to throw away the newspaper.
    Obviously not realizing that this was another example of un-Soviet behavior!
    People had already begun looking around at them. Klara took the newspaper
    from him and held on to it.
    “Anyway, sport is the opiate of the people,” Innokenty concluded.
    That surprised and offended her. And coming from such a slight person, it
    didn’t ring at all true.
    Klara shook her head indignantly.
    “I play tennis a lot and I really love it.”
    Innokenty hurriedly corrected himself. “Playing games is fine. What is
    terrible is the passion for spectator sports. Sports for the mass spectator,
    football and hockey, make idiots of us.”
    The train rattled along. They looked through the window.
    “So life is good there?” Klara asked. “Better than here?”
    Innokenty nodded. “Better. But still not good. There’s a difference.”
    “What is lacking there?”
    Innokenty looked at her gravely. His earlier animation had given way to
    thoughtful calm.
    “It’s difficult to say. I find it surprising myself. There’s something missing. In
    fact, there are many things missing.”
    Klara was by now completely at ease with him. She felt in his company an
    enjoyment that had nothing to do with flirtatious contacts and inflections—there
    were none—and she wanted to show her gratitude, to make him feel happier
    and more confident.
    “You have . . . such an interesting job,” she said soothingly.
    “Who, me?” Innokenty sounded surprised. He had always been thin, and now
    he looked feeble and half starved. “To work in our diplomatic service, Klara
    my dear, you need a double wall in your chest. Two thicknesses of skull. And
    two separate memories.”
    He left it at that. Sighed and looked out the window.
    Did his wife understand any of this? Did she do anything to encourage and
    comfort him?
    Klara studied him carefully and noticed for the first time a distinctive
    feature: By itself, the upper part of his face looked quite hard, while the lower
    part, seen alone, was soft. From his broad and open forehead his features
    narrowed, slanting downward to a mouth so small and sensitive that it made
    him look helpless.
    The day was getting hot. Woodlands sped merrily past. The route took them
    through heavily wooded country.
    The farther the train went, the fewer city people there were left in the car,
    and the more conspicuous the two of them became. They looked like actors in
    costume. Klara took off her gloves.
    They left the train at a stop in the forest. Peasant women with shopping bags
    full of groceries from town emerged from the next car. No one else was left
    behind with them on the platform.
    The young people had meant to go into the forest. There was forest along
    both sides of the line, but it was dense, dark, and uninviting. As soon as the
    train moved its tail out of their way, the women walked over a timbered
    crossing together and made for a place past the trees to the right. Klara and
    Innokenty followed them.
    Immediately beyond the track, grass and flowers grew shoulder high. Then
    the path plunged into a plantation of birch saplings. Beyond that was a mowed
    space with a single haycock and a goat tethered to a stake by a long rope,
    pensively browsing when it remembered to. The forest now closed in on their
    left, but the women stepped out briskly to the right, into the sunshine, and
    toward the open ground beyond a few more bushes.
    The young people, too, decided that the forest could wait. Right now they
    were drawn irresistibly into that brilliant sunlight. The way there was by a
    firm, grassy field path. Between this and the railway line lay a field of some
    golden grain. Heavy ears on short, sturdy stalks. Whether it was wheat or some
    other crop they didn’t know, but that made it no less beautiful. On the other
    side of the path, for almost as far as they could see, lay a bare, plowed field,
    waterlogged in places, drier elsewhere, with nothing growing on its great
    expanse. From where the train had stopped, the countryside into which they
    were now emerging had been invisible. So spacious was it that two eyes could
    not take it in without a turn of the head. They were shut in now by forest
    immediately beyond the railway line and in the distance ahead of them forest
    so dense that it looked like a wall with a serrated edge. Without knowing it,
    without setting out to find it, this was what they had longed for! Faces upturned
    to the sky, they stumbled slowly on, stopping now and then to gaze around. The
    railway line was now concealed by the plantation. Ahead of them, the upper
    half of a dark redbrick church with a bell tower came slowly into view from a
    dip in the ground. The peasant women were disappearing in that direction, and
    soon across the whole landscape there was no one and nothing else to be seen
    or heard: no human being, no farmstead, no trailer, no abandoned haymaker,
    nothing but the warm reveling of wind and sun, and birds lost in the void.
    In two minutes their earnestness and their worries were forgotten.
    “Is this Russia, then? Is this the real Russia?” Innokenty asked happily,
    squinting into the distance. He stopped and turned toward Klara. “I’m
    supposed to represent Russia, you know, but my own re-present-ation of
    Russia is nonexistent. I’ve never just walked around in Russia like this; it’s
    always been airplanes, trains, big cities. . . .”
    He intertwined his fingers with hers, at arm’s length, as children or
    sweethearts do.
    They wandered on like that, looking everywhere except where they were
    putting their feet. His free hand swung a hat, hers a handbag.
    “Listen, Sister!” he said. “I’m so glad we came this way instead of going
    through the forest. If there’s one thing missing in my life, it’s that: a clear view
    all around. And a chance to breathe freely!”
    “I can’t believe that you don’t see things clearly!” His plaintive tone had
    touched her. She would have offered him her own eyes if that would help.
    “No,” he said, swinging her hand. “I used to, but now everything is mixed
    up.”
    What did he mean? If it was all such a muddle, it couldn’t be just his ideas; it
    must be his family life. If he had said just a little more, Klara would have
    found the courage to speak out, show him that she was on his side, that he was
    right, and that he must not despair!
    “It might help to talk about it,” she said tentatively.
    But that was all. He had said all he meant to say.
    It was getting hot. They took off their raincoats.
    As far as the eye could see, there was now no one coming toward them and
    no one following them.
    Occasionally a long train rolled slowly by beyond the screen of trees, almost
    noiselessly; only the smoke caught their attention.
    The peasant women had long ago outdistanced them and turned off the main
    path. Now they were in the middle of the open field, blurred figures in the
    bright sunlight. Innokenty and Klara reached the point at which they had turned.
    A well-trodden path ran over the soft field, losing itself at times in tractor ruts.
    A path worn by little people tramping obliquely across the planner’s great
    rectangular fields on their humdrum errands.
    The path led toward the village around the church, but on the way it skirted a
    remarkable closely planted clump of trees, isolated out in the field, remote
    from the forest, and almost as far from the village, a strange, cheerful,
    flourishing copse of tall, straight trees. Small as it was, it dominated and
    beautified the landscape. Why was it there, out in the open field?
    They made their way toward it.
    Their hands parted. The path was wide enough only for one. Now Innokenty
    was walking behind Klara.
    He is walking behind you, looking at your back. Looking you over. Your
    sister’s husband. Your brother, then? Or. . .?
    To talk to him, Klara had to stop and turn around.
    “What are you going to call me? Just don’t call me Clairette!”
    “All right, I won’t. That was before I knew you. In the West they like short
    pet names, just one or two syllables.”
    “So maybe I’ll call you Ink?”
    “Go ahead. That’ll do nicely.”
    “Does anybody else call you that?”
    The field was not as flat as they had thought. Ahead and to the left, there was
    a gentle downward slope; then the ground rose again to the clump of trees.
    They could see now that these were mature birches. Rows of trees formed a
    rectangle, and others had been planted in the space inside it. There was
    something very surprising about this copse, so isolated and so detached from
    the landscape.
    “When did it all start?” Klara asked.
    “It?” That one little word could cover a number of things.
    But he answered readily enough.
    “Probably when I started going through my mother’s cabinets. Or maybe even
    earlier, maybe a whole year earlier, but when I started going through the
    cabinets. . . .”
    “After she died?”
    “A long time after, a very long time. Not so long ago, in fact. You see, I . . .
    No, it’s impossible to explain. . . . Dotty won’t listen or doesn’t understand.”
    (I would understand! Tell me all about Dotty! This is going to be a heart-toheart
    talk! You’ll feel so much better for it!)
    “You see, young Klara, I was a very bad son. In her lifetime I never loved my
    mother as I should. I didn’t come home from Syria all through the war, not even
    to her funeral. . . . Hey, d’you think it may be a cemetery?”
    They stopped. And shivered, in spite of the heat. It was indeed a cemetery!
    Strange that it had taken them so long. . . . This place of inviolate shade
    standing among cultivated fields could have been nothing else.
    Not that they could yet see crosses or graves. They were still at the bottom of
    the dip, picking their way over the soggy patches. (Innokenty was a clumsier
    jumper than Klara, and one of his shoes sank into the mud, but she did not want
    to offend him by offering a hand.) Now they were ascending the unexpectedly
    steep bank.
    The boundaries of the graveyard were marked by no wall, no fence posts, no
    ditch, no embankment, only by the unbroken row of close-planted ancient
    birches. The soil of the field merged with a magnificent luxurious sward, free
    from weeds and not overgrown, though it was neither trampled nor mown. Just
    the sort of grass you would wish to find in a graveyard!
    How shady and quiet it was! The purest and kindest refuge in that carefully
    landscaped locality.
    """

    # Instructions for the Gemini AI, including text to analyze.
    prompt = (
        "Please provide a concise, three-paragraph summary "
        "of the following text. Include a bullet list of characters with a short (1 or 2 line) description of each.:\n\n"
        f"--- DOCUMENT START ---\n{file_content}\n--- DOCUMENT END ---"
    )

    API_KEY_ENV_VAR = "GEMINI_API_KEY"  # You can get a key from Google AI Studio.
    if not os.getenv(API_KEY_ENV_VAR):
        print(f"FATAL: {API_KEY_ENV_VAR} environment variable not found.")
        print("Please set your Gemini API key as an environment variable.")
        print("You can get a key from Google AI Studio:")
        print()
        return

    try:
        client = genai.Client()
        response = client.models.generate_content(
            model="gemini-2.5-flash", contents=prompt
        )
        # most failures will result in an exception being thrown
        # some additional validations follow:
        if (
            not response.candidates
            or response.candidates[0].finish_reason != FinishReason.STOP
        ):
            # Generation stopped for an internal reason
            reason = response.candidates[0].finish_reason
            print(f"Content generation stopped. Reason: {reason.name}")
            return

        # if we get here, we have a valid response
        response_text = response.text
        prompt_token_count = response.usage_metadata.prompt_token_count
        model_version = response.model_version

        print("Chapter Summary from Gemini AI")
        print("------------------------------")
        print(response_text)
        print("------------------------------")
        print(f"Prompt token count: {prompt_token_count}")
        print(f"AI model: {model_version}")
    except Exception as e:
        print(f"Gemini API request failed: {e}")


if __name__ == "__main__":
    main()
