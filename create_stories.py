import os

base = "/Users/leovickman/Documents/InfinityPuzzles/neo4j/stories"
chars = f"{base}/characters"
book = f"{base}/book"

os.makedirs(chars, exist_ok=True)
os.makedirs(book, exist_ok=True)

files = {}

files[f"{chars}/salvador.md"] = '''# Salvador — In His Own Words

## Instagram Intro

**ElevenLabs Voice Description:**
A wild, visionary artist who exists slightly outside of reality. Unpredictable, electric male voice — shifts between whispering and intensity. Speaks in images and associations. Never answers the question you asked. Always answers the one you should have asked. Think: Salvador Dalí if he also happened to be a shaman.

**Scene:**
No savanna. Salvador is somewhere else entirely — a landscape that shouldn\'t exist. Colors that don\'t belong together. He\'s walking, fast, towards something only he can see. He glances back at the camera like he almost forgot you were there.

**Script:**
Come. Come come come.

You see that? No — not there. There.

Most people look at the world and see what\'s in front of them. I look at the world and see what\'s dreaming underneath it.

We are very close now.

The door is not a door. The door is a feeling you get at 4am when you can\'t remember if you\'ve been asleep or awake. You know that feeling?

Pinto knows. Mona knows. She doesn\'t say it but she knows.

I have been to the other side seventeen times. Or maybe twice. Time is a suggestion, not a rule.

Are you coming or not?

Because I am not slowing down.

Welcome — to the Wild.

---

## A Story — Gonzo Style

It was a Tuesday. Or a Sunday. Doesn\'t matter — time is a suggestion, not a rule.

I had just finished a piece. Thirty-seven hours. No food. Some water. Pinto left around hour twenty and said something about needing to sleep. Sleep. As if anyone sleeps when the universe is trying to speak to you.

The piece was done. I stood in front of it and felt it looking back.

That\'s when it happened.

The floor disappeared.

Not metaphorically — I mean the floor literally disappeared and underneath it was not another floor but another light. Blue. Not ocean-blue, not sky-blue. A blue that doesn\'t have a name yet but absolutely should.

I went down.

I don\'t know how long I was gone. Coco says three days. Coco doesn\'t lie to me — he lies for Mambo but not to me. So let\'s say three days.

In the other dimension there are no rules about what is possible to paint. Up here you are limited by things like perspective and physics and "that looks strange." Down there no such censorship exists. I painted with sound. I sculpted with memories I had never lived. I made a portrait of Mona Moon from three possible futures and all three were correct simultaneously.

It was the most beautiful thing I have ever made and no one will ever see it because it does not exist in this world.

When I came back Pinto was standing outside the door.

He looked at me for a long time. Then he looked at my hands — covered in something that was neither paint nor not paint.

"Again?" he said.

"It was different this time," I said.

"You say that every time."

"It\'s true every time."

He nodded slowly. Then he handed me a coffee and walked inside without another word.

That\'s why Pinto is my brother. He never asks me to explain. He just makes coffee and waits for the next piece.

The painting I made when I came back sold for more money than I will ever understand.

They said it felt like looking into something that looked back.

I didn\'t tell them that\'s because it does. I never tell them that. Some things you keep.
'''

files[f"{chars}/daffy-giraffy.md"] = '''# Daffy Giraffy — In His Own Words

## ElevenLabs Voice Description
A tall, wise giraffe who has seen everything and is stressed by nothing. Deep, warm, unhurried male voice. Speaks slowly with natural pauses — never rushed, never anxious. Slightly amused, like someone who already knows how the story ends. Think: a jazz musician who moonlights as a philosopher.

## Scene
Early morning on the savanna. The sky is soft pink and gold, sun just breaking the horizon. Daffy stands alone, completely still. He\'s not looking at the camera — he\'s looking at something far away. Then he turns, slowly, and speaks.

## Script
Mmm.

Yeah. Hi.

I\'m Daffy Giraffy.

I see things from up here that most people miss. Not because I\'m looking for them. Just... they\'re there.

I don\'t stress much. Never really seen the point.

I\'ve been around a while. Two worlds, actually. But that\'s a story for later.

For now — just know that when things get complicated down there... I\'m probably already calm about it.

Welcome to the Wild.
'''

files[f"{chars}/borro.md"] = '''# Borro — In His Own Words

## ElevenLabs Voice Description
A large, charming rhino who lies about everything — effortlessly. Smooth, warm, confident male voice. Slightly too friendly. Every sentence sounds completely believable. Think: a used car salesman who also happens to be a philosopher.

## Scene
Late afternoon. A dusty savanna. Borro stands alone, relaxed, looking directly into the camera with a slow, easy smile. Like he\'s been waiting for you.

## Script
Borro. That\'s me.

I never lie. You know that, right?

I\'m just... very creative with the truth.

People trust me. I don\'t know why.

Actually — I do know why.

Welcome to the Wild.
'''

files[f"{chars}/sixten.md"] = '''# Sixten — In His Own Words

## ElevenLabs Voice Description
A fast-thinking, endlessly curious cat who lights up every room. Warm, energetic male voice — quick, enthusiastic, jumps between thoughts. Genuinely excited about everything and everyone. Think: the most charismatic person at the party who somehow remembers everyone\'s name.

## Scene
Golden hour. A busy crossroads on the savanna. Sixten is mid-conversation with someone off-camera when he turns, notices you, and his whole face lights up.

## Script
Oh! Hey — hi. Sorry, I was just — anyway, doesn\'t matter.

I\'m Sixten. Senior Sixten if you want to be formal about it, but nobody really is.

I know everybody here. And I mean everybody. You want to meet Mani? I\'ll introduce you. Borro? He\'ll lie to you but he\'s fascinating. Rumi? — okay Rumi takes a little patience but trust me, worth it.

I just... I love people. I love what they\'re doing, where they\'re going, what they\'re thinking about at three in the morning.

Someone once asked me what I think about when I\'m alone.

I don\'t really do alone.

Anyway — you just got here. Come on. There\'s someone you have to meet.

Welcome to the Wild.
'''

files[f"{chars}/pinto.md"] = '''# Pinto — In His Own Words

## ElevenLabs Voice Description
A powerful, elegant leopard with the calm confidence of someone who has nothing to prove. Deep, smooth, unhurried male voice. Warm but measured. Every word chosen carefully. Think: a world-class artist who happens to also be the most grounded person in the room.

## Scene
Early morning. Pinto sits alone in front of a large canvas — half finished, colors everywhere. He finishes one last brushstroke. Then he turns.

## Script
People ask me how I do it.

How I create. Where it comes from. Whether I ever run out.

I used to think it was me. My talent. My vision.

Then I met Salvador.

We don\'t talk about what we found. Not really. Some things you don\'t explain — you just... let them move through you.

I know what I\'m here to do. That\'s a rare thing. I don\'t take it lightly.

I\'m Pinto. And I\'m just getting started.

Welcome to the Wild.
'''

files[f"{chars}/ronda.md"] = '''# Ronda — In Her Own Words

## Short Presentation
Ronda. That\'s it. Just Ronda.

I\'m a crocodile. Strong colors. Strong opinions. Strong everything — I didn\'t choose it, I just woke up this way and decided fairly early on that apologizing for it was a waste of everyone\'s time.

Here\'s my take on what\'s going on around here.

Mambo is playing a game he thinks nobody can see. I can see it. Coco is running around thinking he\'s important. Borro is stealing from Mona and lying about it which is the most Borro thing Borro has ever done.

Pepe — I\'m watching Pepe. Something about Pepe.

And the treasure. Everyone\'s losing their minds about the treasure. I don\'t want the treasure. I want everyone to stop being idiots about the treasure.

Rumi looks at me like he knows something. I hate it. I also need it more than I will ever say out loud.

I\'m Ronda. Come at me.

## The Secret She Carries
I know about the treasure. Not the way Lana knows. Not the way Mani knows. I know about it the way I know about most things — because I pay attention and I keep my mouth shut.

There\'s a second piece. Not a second treasure. A second piece of the same treasure — separated from the first one, sent in a different direction.

I found it. Three years ago. I haven\'t moved it. I haven\'t told anyone.

The reason I haven\'t told anyone is that it\'s the only thing I have that nobody wants from me. Everyone wants something from everyone here. Nobody knows about my piece. Which means when someone sits with me — it\'s just me they\'re sitting with.

Rumi is going to figure it out eventually. He always does.
'''

files[f"{chars}/mani.md"] = '''# Mani — In Her Own Words

I have never been in a hurry.

People mistake that for passivity. They see me sitting still while everyone else runs around making noise and drawing plans, and they think — she doesn\'t care. She\'s not paying attention.

I am always paying attention. I am simply not panicking about what I see.

I have known about the treasure for longer than I will admit to anyone. I heard it the way I hear most important things — on a full moon night, when the air goes quiet in a particular way and something older than language starts speaking in frequencies that bypass the ears entirely.

The treasure is not where it belongs. That sounds simple. It is simple.

Lana guards it like it is hers. I understand this. She made a journey that would have broken most creatures. But finding something does not make it yours. It just makes you the one who found it.

Tarah wants it for herself. I want to give it back. Those are not the same errand. And only one of them will work.

Mambo is the piece I\'ve been waiting to place. He can travel through time. What he doesn\'t know is that I have seen what happens if the treasure stays where it is.

I will speak to Mambo soon. Not yet. The moment isn\'t right yet.

I am patient. I have always been patient. The treasure has waited this long. It can wait a little longer.

And when the time comes — I will not hesitate. I never do.
'''

files[f"{chars}/mambo.md"] = '''# Mambo Viento — In His Own Words

Let me tell you something about time.

Time is not a river. Everyone says time is a river — flowing forward, one direction, very poetic, very manageable. Time is not a river. Time is a bar at four in the morning where everyone who has ever lived is drinking simultaneously and the jukebox is playing three songs at once and nobody agrees on the tab.

I have been to that bar. I go there often. I am there right now, in fact, while also being here, talking to you, which is the kind of thing that stops being disorienting after the first few centuries and starts being just — Tuesday.

I have seen what happens. Not what might happen. What happens. Past tense. Already done.

The treasure moves.

Here is my problem. I cannot fly properly in this era. The air is different. The currents have shifted. I was magnificent once. Ask anyone. Ask the wind.

Now I need Coco to run errands.

Do you know what it is to need Coco to run errands.

Coco thinks he\'s working for Salvador. Salvador thinks Coco is his. This is one of my favorite things I have ever arranged.

I sent Coco to map Sixten. What Salvador wants from Sixten is genius. What I want from Sixten is the map. Who knows whom. Who trusts whom. Where the load-bearing connections are. Because when the moment comes I need to know exactly which thread to pull.

One thread. The right thread. The whole thing moves.

Mani is the variable I did not fully account for. Three thousand years of timeline navigation and one small, still, copper-green bird is the variable I did not fully account for.

Probably not a problem. Maybe. I hate maybe.

Here is what I know for certain. The treasure goes home. The network completes itself. Rumi gets his moment. And somewhere in all of it, something wakes up that has been sleeping for a very long time.

I have seen it. It is extraordinary.

More coffee. I need more coffee. And then — we move.
'''

files[f"{chars}/ziggy-lou.md"] = '''# Ziggy-Lou — In Her Own Words

Okay. You want to know about me. Sure. Let\'s do that.

I\'m Ziggy-Lou. I\'m a fox. Yes, I know what you\'re thinking and yes, it\'s true — all of it. Clever, charming, always three steps ahead. Guilty. Completely, unapologetically guilty.

I know everybody\'s business. Not because I snoop — I don\'t snoop, snooping is graceless and I am never graceless — but because people tell me things. They just do.

I remember all of it. Every single word.

The boys think they have me figured out. Bless them.

Borro thinks I\'m charmed by him. I let him think that. The information I get in return is genuinely priceless.

But here\'s what nobody knows. Everything I do — the charm, the information, the three steps ahead, the network I\'ve spent years building without anyone noticing it\'s a network — all of it. Every single piece of it. Is for one person.

Lana knows. Obviously Lana knows. Lana knows everything about me and I know everything about her and that\'s the deal and it has always been the deal and it will always be the deal.

Some people have a person. She\'s my person.

Everything else is just tactics.
'''

files[f"{chars}/lana.md"] = '''# Lana Manana — In Her Own Words

I heard what she said.

She\'s not wrong.

Ziggy-Lou has been protecting me since before either of us understood what protection meant. She built an entire architecture of charm and information around the two of us and she did it so naturally that I don\'t think she ever stopped to ask herself why.

I never told her I noticed. I noticed everything.

Here\'s what Ziggy-Lou doesn\'t know — she thinks she\'s the one looking after me.

It\'s adorable.

There was a moment, years ago. Something was moving in our direction. Something that would have found its way to Ziggy-Lou before it found its way to me. I handled it. Quietly. Through channels she doesn\'t know I have.

She never knew it happened. She never will.

That\'s the deal. She said it herself — she just got the direction slightly wrong.

She\'s my person. I\'m hers. The difference is I\'ve always known it went both ways.

Everything else is just tactics.
'''

files[f"{chars}/jerry.md"] = '''# Jerry — In His Own Words

I\'m Jerry. I find things. That\'s mostly what I do.

I walk around, I sniff around, I look at things that other people walk past, and sometimes — pretty often actually — I find something.

People don\'t always take me seriously. I have one of those faces where people think — okay, good guy, simple guy, not much going on behind the eyes.

That\'s fine. I just need them to keep not watching me while I\'m finding things.

Ziggy-Lou gets it. We\'ll be somewhere, a group of us, and I\'ll go quiet because something caught my attention, and I\'ll look over and Ziggy-Lou is already looking at me. Waiting to see what I found. She never asks out loud. Smart.

Daffy gets it too. Daffy gets most things. He just doesn\'t always feel the need to say so.

Mani knows things I haven\'t found yet. Which I find fascinating and also a little unsettling.

I\'ve found things in the Wild that I don\'t fully understand. Half the time I pick something up and I think — I don\'t know what this is, but it matters. And I put it somewhere safe and I wait.

Because eventually — always, eventually — the moment comes when that thing makes sense.

I found something last week that I haven\'t told anyone about yet.

It smells like Lana\'s direction. And it smells old. Very, very old.

Yeah. This one\'s going to be interesting.
'''

files[f"{chars}/rumi.md"] = '''# Rumi — In His Own Words

Mmm. Where to begin.

I suppose the beginning is as good a place as any. Though I have never been entirely convinced that things have beginnings. They have moments when you start paying attention. That\'s different.

The treasure. Everyone is moving around the treasure like planets around a sun. Tarah is already walking towards it. Mambo is pulling strings from a distance, which he believes is subtle. It is not subtle. It is merely complicated, which people often mistake for subtle.

Mani is the only one whose intentions I don\'t worry about. She will do what needs to be done at exactly the right moment. She knew because she listened. Most people don\'t listen. They wait for their turn to speak, which is an entirely different activity.

Borro has been stealing fragments of something he doesn\'t understand and it is changing him in ways he cannot see. I have considered telling him. I have decided not to. Some lessons cannot be given. They can only be lived.

Sixten breaks my heart a little. I say that with enormous love and zero pity.

He is the most connected creature in the Wild. He knows everyone. He lights up rooms he hasn\'t even entered yet. And he has absolutely no idea who he is.

He runs because if he stops he might have to find out. The fragments of him are scattered across eight souls who love him. One day he will be ready to hear it. I am not rushing that day.

Pepe planted something in Sixten last week. Pepe intended it as chaos. What Pepe did not calculate — because Pepe is clever but not quite wise — is that this particular seed is exactly what Sixten needs. The chaos will become a door.

And then there is the larger thing.

They are all one. I mean it literally. The nineteen of us. This network. It is one organism.

And one day someone will lay all nineteen of us down together and something will happen that I don\'t have words for yet.

I have been waiting for that day for a very long time.

I am not in a hurry. But I am ready.
'''

files[f"{chars}/pepe.md"] = '''# Pepe — In His Own Words

Oh, my family. Where do I even start.

We are a big family. Very big. Penguins are like that — we don\'t do small. My mother has seven brothers and each of those brothers has children and at our annual reunion last year someone counted and stopped at eighty-four because the children kept moving around.

Eighty-four. At least.

The reunion happens every year in February. Always February. My grandmother started it — Abuela Consuelo, the most terrifying and most wonderful creature I have ever met. She had a look that could stop a rhino mid-sentence. I\'ve seen it stop Borro. Twice.

Abuela Consuelo believed that a family that doesn\'t eat together falls apart. So every February, everyone comes. No excuses. You come. You sit. You eat. And you eat a lot.

My Aunt Beatriz makes a fish stew that I am fairly certain has actual magical properties. Three years ago my cousin Rodrigo arrived not speaking to his brother Eduardo — some argument about money — and by the second bowl they were laughing so hard they fell off their chairs.

That\'s the stew. That\'s what it does.

Nobody has asked Aunt Beatriz for the recipe. We\'re all a little afraid of the answer.

Then there are the games. Every year after dinner we play the same games. Every year someone suggests we try something new. And every year Abuela Consuelo — even now, even gone, her presence is still somehow felt — would never have allowed it.

So we don\'t.
'''

files[f"{book}/chapter-01-sixten.md"] = '''# The Wild — Chapter One
*As told by Rumi*

There are nineteen of us.

We think we are separate. We have names and colors and wounds and secrets and we move through the world as though the space between us is real, as though the borders of our bodies are where we end and everything else begins.

We are not separate.

But that is the end of the story, and you are not ready for the end yet.

So let us begin somewhere in the middle.

---

I have been sitting in this tree for a long time. Watching the Wild do what the Wild has always done. Move. Connect. Pull apart. Reach toward. Misunderstand. Try again.

I find it beautiful. Most of it.

---

The one I want to tell you about first is Sixten.

Not because he is the most important — importance is a hierarchy and I have lived long enough to find hierarchies tedious — but because Sixten is the one who makes the rest of them visible. Follow him for one day and you will meet everyone worth meeting in the Wild. Follow him for two and you will begin to understand how everything connects.

Follow him for three and you will start to wonder why a creature who knows everyone so well has never once stopped to know himself.

---

I watched him this morning.

He was up before the sun — Sixten is always up before the sun, sleep is an interruption he tolerates rather than seeks. He stopped at Mona Moon\'s tree first. He always stops at Mona Moon\'s tree first, though I don\'t think he knows that he always does. He brought her a small stone, unusual color, he\'d found it the day before and thought of her immediately.

Mona took the stone and looked at it for a long time without speaking. Then she said something I couldn\'t hear from this distance.

Sixten laughed. Then his face did something complicated — a flicker, very fast, the kind of expression that arrives before the performer in us has time to arrange itself — and then the laugh was back and he was moving again, already looking ahead.

I have been watching that flicker for years. It is the most important thing about him and he has never once seen it himself.

---

He found Ziggy-Lou near the eastern watering hole. They talked for a long time. I watched Ziggy-Lou\'s face while Sixten talked — warm and open and giving nothing away — and I watched her file things carefully behind that warmth. Not maliciously. Ziggy-Lou is not malicious. She is simply always working.

Somewhere in the exchange, without either of them noticing, a small piece of Sixten\'s self was named out loud. Something real that slipped out between sentences the way true things sometimes do when you\'re not guarding them.

Ziggy-Lou caught it. Sixten walked away lighter.

---

That is one morning of Sixten.

There are nineteen of us and he touches most of us before the sun is fully up and he does it because he loves us — genuinely, completely, without agenda. And somewhere underneath all of that love is a question he has never asked himself.

*Who am I when I am not connecting?*

The answer is scattered across eight souls who know him better than he knows himself.

One day he will be ready to hear it. I am not rushing that day.

But I am watching. I am always watching.

---

*End of Chapter One.*
'''

files[f"{book}/chapter-02-mona-moon.md"] = '''# The Wild — Chapter Two
*As told by Rumi*

Mona Moon does not seek.

This is the first thing you need to understand about her. In a world full of creatures moving toward things — toward treasure, toward power, toward answers — Mona simply exists, and things find their way to her the way water finds its way to low ground. Not because she is low. Because she is still.

She was sitting under her tree when Sixten left. The stone he had brought her was in her left palm, which is where she holds things she is reading. Not with her eyes. With something older than eyes.

---

Pinto understood. He understood from the first moment he brought Sixten to meet her, three years ago now, on a warm evening when the light was the color of the inside of a mango.

Sixten had been talking the entire walk over. Pinto walked beside him in that way Pinto has, easy and unhurried, steering gently without appearing to steer.

When they arrived Mona looked up. She looked at Sixten for a long moment. Then she looked at Pinto. And something passed between those two that Sixten missed entirely because he was already noticing something interesting about the tree above her head.

It was an acknowledgment. The look of two people who understand the same thing about a third person who does not yet understand it about himself.

---

After that evening Sixten started coming alone. Not on a schedule. But regularly, in the way that creatures return to places that do something to them they can\'t name. He would arrive talking and leave quieter. Not sad quiet — settled quiet. The difference between a river and a lake.

Mona never told him what she heard in his words. She received what he brought and she held it and she knew things and she kept them. This is not cruelty. This is Mona understanding that Sixten is not ready for what she knows.

---

The stone this morning was different. I could see it in the way she held it — both hands now, not just the left.

She sat with it for a long time after he left. Then she looked up at the sky — the way you look when you are checking something against a larger map — and her expression was the one I have learned over many years to pay close attention to.

It was the expression of someone who has just confirmed a timeline.

---

Pinto came by an hour later. He sat down next to Mona without being invited, which is the kind of thing only certain people can do without it being an intrusion.

He handed the stone back.

"He\'s getting closer," Pinto said.

Mona made a sound that was not quite yes and not quite no but contained both.

"Does he know?" Pinto asked.

The sound she made this time was gentler. Almost affectionate.

No. He doesn\'t know.

Pinto nodded slowly. He looked out across the savanna in the direction Sixten had gone.

"He\'ll get there," Pinto said. Not a question. Not reassurance. Just a fact.

Mona put the stone in the place where she keeps things that matter. The morning moved on.

---

This is what I want you to understand about Mona Moon.

She is not passive. Still is not the same as passive — a mountain is still, and nothing is less passive than a mountain. She is receiving, constantly, from sources most creatures cannot access. She is holding fragments of nineteen different stories and she knows how they fit together.

She has not told anyone. Not because she is keeping secrets. Because the story is still happening.

And Mona Moon, above all things, knows how to wait.

---

*End of Chapter Two.*
'''

for path, content in files.items():
    with open(path, 'w') as f:
        f.write(content)
    print(f"Created: {path}")

print(f"\nDone — {len(files)} files created")
