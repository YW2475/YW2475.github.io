#import "../index.typ": template, tufted
#import "../../_essay/bilingual.typ": zh
#show: template.with(
  title: "Geometry for the Selfish Herd",
  author: "W. D. Hamilton",
  date: "1971",
  description: "动物各自躲避捕食者时，怎样形成看似团结的兽群？",
  lang: "en",
  css: ("/assets/custom.css", "/assets/essay.css"),
)

= Geometry for the Selfish Herd / 自私兽群的几何学

#html.p(id: "en-S001")[#text("This paper presents an antithesis to the view that gregarious behaviour is evolved through benefits to the population or species. Following Galton")]

#zh(id: "S001")[#text("本文提出了一种观点的对立面，即群居行为是通过对种群或物种的好处而进化的。关注高尔顿")]

#html.p(id: "en-S002")[#text("(1871) and Williams (1964) gregarious behaviour is considered as a form of cover-seeking in which each animal tries to reduce its chance of being caught by a predator.")]

#zh(id: "S002")[#text("(1871) 和 Williams (1964) 群居行为被认为是一种寻求掩护的形式，其中每只动物都试图减少被捕食者捕获的机会。")]

#html.p(id: "en-S003")[#text("It is easy to see how pruning of marginal individuals can maintain centripetal instincts in already gregarious species; some evidence that marginal pruning actually occurs is summarized. Besides this, simply defined models are used to show that even in non-gregarious species selection is likely to favour individuals who stay close to others.")]

#zh(id: "S003")[#text("很容易看出边缘个体的修剪如何能够在已经群居的物种中维持向心本能；总结了一些实际发生边缘捕杀的证据。除此之外，简单定义的模型表明，即使在非群居物种中，选择也可能有利于与其他物种保持密切关系的个体。")]

#html.p(id: "en-S004")[#text("Although not universal or unipotent, cover-seeking is a widespread and important element in animal aggregation, as the literature shows. Neglect of the idea has probably followed from a general disbelief that evolution can be dysgenic for a species. Nevertheless, selection theory provides no support for such disbelief in the case of species with outbreeding or unsubdivided populations.")]

#zh(id: "S004")[#text("正如文献所示，虽然寻找掩护并不普遍或单能，但它是动物聚集中广泛且重要的因素。对这个想法的忽视可能是因为人们普遍不相信进化可能对一个物种造成基因不良。然而，对于具有远交或未细分种群的物种，选择理论并没有为这种怀疑提供支持。")]

#html.p(id: "en-S005")[#text("The model for two dimensions involves a complex problem in geometrical probability which has relevance also in metallurgy and communication science. Some empirical data on this, gathered from random number plots, is presented as of possible heuristic value.")]

#zh(id: "S005")[#text("二维模型涉及几何概率中的复杂问题，该问题也与冶金和通信科学相关。从随机数字图中收集的一些经验数据被呈现为可能的启发价值。")]

== 1. A Model of Predation in One Dimension / 1. 一维捕食模型

#html.p(id: "en-S006")[#text("Imagine a circular lily pond. Imagine that the pond shelters a colony of frogs and a water-snake. The snake preys on the frogs but only does so at a certain time of day-up to this time it sleeps on the bottom of the pond. Shortly before the snake is due to wake up all the frogs climb out onto the rim of the pond. This is because the snake prefers to catch frogs in the water. If it can’t find any, however, it rears its head out of the water and surveys the disconsolate line sitting on the rim-it is supposed that fear of terrestial predators prevents the frogs from going back from the rim-the snake surveys this line and snatches the nearest one.")]

#zh(id: "S006")[#text("想象一个圆形的荷花池。想象一下池塘里栖息着一群青蛙和一条水蛇。这条蛇捕食青蛙，但只在一天中的特定时间捕食——直到这个时候它才会睡在池塘底部。就在蛇醒来前不久，所有的青蛙都爬到了池塘的边缘。这是因为蛇更喜欢在水中捕捉青蛙。然而，如果它找不到任何东西，它就会把头伸出水面，观察边缘上那条令人沮丧的线——人们认为，对陆地捕食者的恐惧阻止青蛙从边缘返回——蛇观察这条线并抓住最近的一条。")]

#html.p(id: "en-S007")[#text("Now suppose that the frogs are given opportunity to move about on the rim before the snake appears, and suppose that initially they are dispersed in some rather random way. Knowing that the snake is about to appear, will all the frogs be content with their initial positions? No; each will have a better chance of not being nearest to the snake if he is situated in a narrow gap between two others. One can imagine that a frog that happens to have climbed out into a wide open space will want to improve his position. The part of the pond’s perimeter on which the snake could appear and find a certain frog to be nearest to him may be termed that frog’s “domain of danger” : its length is half that of the gap between the neighbours on either side. The diagram below shows the best move for one particular frog and how his domain of danger is diminished by it:")]

#zh(id: "S007")[#text("现在假设在蛇出现之前青蛙有机会在边缘移动，并假设最初它们以某种相当随机的方式分散。知道蛇即将出现，所有的青蛙都会满足于自己最初的位置吗？不;如果每个人都位于另外两个人之间的狭窄间隙中，那么每个人都有更好的机会不离蛇最近。可以想象，一只青蛙碰巧爬到了一片开阔的空间里，它会想要改善自己的位置。池塘周边的那部分蛇可能会出现并找到离他最近的某只青蛙，这部分可以称为该青蛙的“危险域”：它的长度是两侧邻居之间间隙的一半。下图显示了一只特定青蛙的最佳动作以及它的危险范围如何因此而减小：")]

#html.figure(id: "F001", class: "essay-paper-figure")[
  #image("assets/figure-01.png")
]

#html.p(id: "en-S008")[#text("But usually neighbours will be moving as well and one can imagine a confused toing-and-froing in which the desirable narrow gaps are as elusive as the croquet hoops in Alice’s game in Wonderland. From the positions of the above diagram, assuming the outside frogs to be in gaps larger than any others shown, the following moves may be expected:")]

#zh(id: "S008")[#text("但通常邻居也会移动，人们可以想象一种混乱的来回，其中理想的狭窄间隙就像爱丽丝梦游仙境游戏中的槌球篮一样难以捉摸。根据上图的位置，假设外侧青蛙的间隙大于所示的任何其他青蛙，则可能会出现以下移动：")]

#html.figure(id: "F002", class: "essay-paper-figure")[
  #image("assets/figure-02.png")
]

#html.p(id: "en-S009")[#text("What will be the result of this communal exercise ? Devious and unfair as usual, natural justice does not, in general, equalize the risks of these selfish frogs by spacing them out. On the contrary, with any reasonable assumptions about the exact jumping behaviour, they quickly collect in heaps. Except in the case of three frogs who start spaced out in an acuteangled triangle I know of no rule of jumping that can prevent them aggregating. Some occupy protected central positions from the start; some are protected only initially in groups destined to dissolve; some, on the margins of groups, commute wildly from one heap to another and yet continue to bear most of the risk. Figure 1 shows the result of a computer")]

#zh(id: "S009")[#text("这次集体演习会产生什么结果？与往常一样，自然正义是狡猾和不公平的，一般来说，自然正义不会通过将这些自私的青蛙分开来平衡它们的风险。相反，只要对确切的跳跃行为有任何合理的假设，它们就会很快聚集成堆。除了三只青蛙开始排列成锐角三角形的情况外，我不知道任何跳跃规则可以阻止它们聚集。有些从一开始就占据受保护的中心位置；有些只是最初在注定要解散的团体中受到保护；有些处于群体边缘的人疯狂地从一群人转移到另一群人，但仍继续承担大部分风险。图1为计算机结果")]

#html.figure(id: "F003", class: "essay-paper-figure")[
  #image("assets/figure-03.png")
]

#html.p(id: "en-C001", class: "essay-original-caption")[#text("FIG. 1. Gregarious behaviour of 100 frogs is shown in terms of the numbers found successively within 10° segments on the margin of the pool. The initial scatter (position 1) is random. Frogs jump simultaneously giving the series of positions shown. They pass neighbours’ positions by one-third of the width of the gap. For further explanation, see text simulation experiment in which 100 frogs are initially spaced randomly round the pool. In each “round” of jumping a frog stays put only if the “gap” it occupies is smaller than both neighbouring gaps; otherwise it jumps into the smaller of these gaps, passing the neighbour’s position by one-third of the gap-length. Note that at the termination of the experiment only the largest group is growing rapidly.")]

#zh(id: "C001")[#text("如图。 1. 100只青蛙的群居行为以池边10°范围内连续发现的数量来表示。初始分散（位置 1）是随机的。青蛙同时跳跃，给出所示的一系列位置。他们以间隙宽度的三分之一超过邻居的位置。如需进一步说明，请参阅文本模拟实验，其中 100 只青蛙最初随机分布在水池周围。在每一“轮”的跳跃中，只有当青蛙占据的“间隙”小于两个相邻间隙时，青蛙才会保持原地不动；否则，它会跳入这些间隙中较小的一个，以间隙长度的三分之一超过邻居的位置。请注意，在实验结束时，只有最大的群体正在快速增长。")]

#html.p(id: "en-S010")[#text("The idea of this round pond and its circular rim is to study cover-seeking behaviour in an edgeless universe. No apology, therefore, need be made even for the rather ridiculous behaviour that tends to arise in the later stages of the model process, in which frogs supposedly fly right round the circular rim to “jump into” a gap on the other side of the aggregation. The model gives the hint which I wish to develop: that even when one starts with an edgeless group of animals, randomly or evenly spaced, the seZ@ravoidance of a predator can lead to aggregation.")]

#zh(id: "S010")[#text("这个圆形池塘及其圆形边缘的想法是研究无边宇宙中的寻找掩护行为。因此，即使对于在模型过程的后期阶段往往出现的相当荒谬的行为也无需道歉，在这种行为中，青蛙据称绕着圆形边缘飞行，“跳进”聚集体另一侧的间隙中。该模型给出了我希望发展的提示：即使我们从一群无边的动物开始，随机或均匀间隔，捕食者的 seZ@ravoidance 也可能导致聚集。")]

== 2. Aggregations and Predators / 2. 聚集体和捕食者

#html.p(id: "en-S011")[#text("It may seem a far cry from such a phantasy to the realities of natural selection. Nevertheless I think there can be little doubt that behaviour which is similar in biological intention to that of the hypothetical frogs is an important factor in the gregarious tendencies of a very wide variety of animals. Most of the herds and flocks with which one is familiar show a visible closing-in of the aggregation in the presence of their common predators. Starlings do this in the presence of a sparrowhawk (Baerends & Baerends-van Roon, 1950; Hostman, 1952; Lorenz, 1966; Tinbergen, 1951); sheep in the presence of a dog, or, indeed, any frightening stimulus (Scott, 1945). Parallel observations are available for the vast flocks of the quelea (Crook, 1960), and for deer (Darling, 1937). No doubt a thorough search of the literature would reveal many other examples. The phenomenon in fish must be familiar to anyone who has tried to catch minnows or sand eels with a net in British waters. Almost any sudden stimulus causes schooling fish to cluster more tightly (Breder, 1959), and fish have been described as packing, in the presence of predators, into balls so tight that they cannot swim and such that some on top are thrust above the surface of the water (Springer, 1957). A shark has been described as biting mouthfuls from a school of fish “much in the manner of a person eating an apple” (Bullis, 1960).")]

#zh(id: "S011")[#text("这种幻想与自然选择的现实似乎相去甚远。尽管如此，我认为毫无疑问的是，与假设的青蛙的生物学意图相似的行为是多种动物群居倾向的重要因素。人们所熟悉的大多数牛群和羊群在共同的捕食者面前都表现出明显的聚集状态。椋鸟在雀鹰面前这样做（Baerends & Baerends-van Roon, 1950; Hostman, 1952; Lorenz, 1966; Tinbergen, 1951）；在有狗的情况下，或者事实上，在任何可怕的刺激下，羊都会被吓到（Scott，1945）。可以对大量奎利亚雀（Crook，1960）和鹿（Darling，1937）进行平行观察。毫无疑问，对文献的彻底搜索会揭示许多其他例子。任何在英国水域尝试用网捕捞过小鱼或沙鳗的人都一定熟悉鱼类中的这种现象。几乎任何突然的刺激都会导致成群的鱼更加紧密地聚集在一起（Breder，1959），并且被描述为在捕食者存在的情况下，鱼会挤成球状，以至于无法游泳，以至于顶部的一些被推到水面以上（Springer，1957）。鲨鱼被描述为“像人吃苹果一样”咬住一群鱼（Bullis，1960）。")]

#html.p(id: "en-S012")[#text("G. C. Williams, originator of the theory of fish schooling that I am here supporting (Williams, 1964, 1966) points out that schooling is particularly evident in the fish that inhabit open waters. This fits with the view that schooling is similar to cover-seeking in its motivation. His experiments showed that fish species whose normal environment afforded cover in the form of weeds and rocks had generally less marked schooling tendencies. Among mammals, similarly, the most gregarious species are inhabitants of open grassy plains rather than of forest (Hesse, Allee & Schmidt, 1937). With fish schools observers have noted the apparent uneasiness of the outside fish and their eagerness for an opportunity to bury themselves in the throng (Springer, 1957) and a parallel to this is commonly seen in the behaviour of the hindmost sheep that a sheepdog has driven into an enclosure: such sheep try to butt or to jump their way into the close packed ranks in front. Behaviour of this kind certainly cannot be regarded as showing an unselfish concern for the welfare of the whole group.")]

#zh(id: "S012")[#text("我在这里支持的鱼类成群理论的创始人 G. C. 威廉姆斯 (Williams, 1964, 1966) 指出，成群现象在栖息于开阔水域的鱼类中尤其明显。这符合这样一种观点，即学校教育的动机与寻找掩护相似。他的实验表明，在正常环境中以杂草和岩石形式提供遮盖的鱼类通常没有明显的鱼群倾向。同样，在哺乳动物中，最群居的物种是开阔的草原而不是森林的居民（Hesse，Allee＆Schmidt，1937）。对于鱼群，观察者注意到外面的鱼明显感到不安，并且渴望有机会将自己埋在鱼群中（Springer，1957），与此类似的情况常见于牧羊犬驱赶到围栏中的最后面的羊的行为：这些羊试图撞到或跳进前面紧密拥挤的队伍中。这种行为当然不能被视为表现出对整个群体福祉的无私关心。")]

#html.p(id: "en-S013")[#text("With ungulate herds (Galton, 1871; Sdobnikov, 1935) with bird flocks (Tinbergen, 1951; Wynne-Edwards, 1962) and with the dense and sudden emerging columns of bats that have been described issuing at dusk from great bat caves (Moore, 1948 ; Pryer, 1884) observations that predators do often take isolated and marginal individuals have frequently been recorded. Nor are such observations confined to vertebrate or to mobile aggregations. Similar observations have been recorded for locusts (Hudleston, 1958), for gregarious caterpillars (Tinbergen, 1953a) and, as various entomologists have told me, for aphids.")]

#zh(id: "S013")[#text("有蹄类动物群（Galton，1871；Sdobnikov，1935）和鸟群（Tinbergen，1951；Wynne-Edwards，1962）以及黄昏时从大蝙蝠洞中突然出现的密集而突然出现的蝙蝠群（Moore，1948；Pryer，1884）观察到捕食者确实经常采取孤立和边缘的观察个人经常被记录。这种观察也不限于脊椎动物或移动聚集。对于蝗虫（Hudleston，1958）、群居毛毛虫（Tinbergen，1953a）以及蚜虫（正如许多昆虫学家告诉我的那样），也有类似的观察结果。")]

#html.p(id: "en-S014")[#text("For the aphids some of the agents concerned are not predators in a strict sense but fatal parasites. Insect parasites of vertebrates are seldom directly fatal but, through transmitted diseases or the weakening caused by the activities of endoparasitic larvae, must often cause death indirectly nevertheless. Thus escape from insect attack is another possible reward for gregarious instincts. From observations in Russia, V. M. Sdobnikov (1935) has stated that when reindeer are standing in dense herds only the outermost animals are much attacked by insects. Among the species which he observed attacking the reindeer, those which produced the most serious affliction were nose flies and warble flies, larvae of which are endoparasites of the nasal passages and the skin respectively. Recently Espmark (1968) has verified and extended most of Sdobnikov’s information. His work reinforces the view that such oestrid flies are important and ancient enemies of their various ungulate hosts, as is suggested by the fact that their presence induces a seemingly instinctive terror. Reindeer seem to be almost as terrified of them as they are of wolves, and cattle react as though they feared the certainly painless egg-laying of warble flies far more than they fear the painful bites of large blood-suckers (Austen, 1939).")]

#zh(id: "S014")[#text("对于蚜虫来说，一些相关的媒介并不是严格意义上的捕食者，而是致命的寄生虫。脊椎动物的昆虫寄生虫很少直接致命，但通过传播疾病或内寄生幼虫活动引起的衰弱，通常必然间接导致死亡。因此，逃避昆虫攻击是群居本能的另一种可能的奖励。根据在俄罗斯的观察，V. M. Sdobnikov (1935) 指出，当驯鹿站在密集的群中时，只有最外面的动物容易受到昆虫的攻击。在他观察到的攻击驯鹿的物种中，造成最严重痛苦的是鼻蝇和莺蝇，它们的幼虫分别是鼻腔和皮肤的内寄生虫。最近，Espmark（1968）验证并扩展了 Sdobnikov 的大部分信息。他的工作强化了这样一种观点，即这种雌蝇是其各种有蹄类动物宿主的重要且古老的敌人，正如它们的存在引起看似本能的恐惧这一事实所表明的那样。驯鹿对它们的恐惧似乎几乎和对狼的恐惧一样，而牛的反应就好像它们对莺蝇毫无痛苦的产卵的恐惧远胜于对大型吸血虫的痛苦叮咬（Austen，1939）。")]

#html.p(id: "en-S015")[#text("The occurrence of marginal predation has also been recorded for some of the aggregations formed by otherwise not very gregarious animals for the purpose of breeding. The best data known to me concerns nesting Blackheaded gulls. The work of Kruuk (1964) has been reinforced by further studies, summarized by Lack (1968). The latter seem to have shown that all marginal nests failed to rear young, mainly due to predation. Perhaps, nevertheless, the gulls that could not get places in the centre of the colony were right in nesting on the edge rather than in isolation where, for a conspicuous bird like a gull, the chances would have been even worse.")]

#zh(id: "S015")[#text("一些不太群居的动物为了繁殖而形成的聚集体也记录了边缘捕食的发生。据我所知，最好的数据是关于筑巢的黑头鸥。 Kruuk (1964) 的工作通过 Lack (1968) 总结的进一步研究得到了加强。后者似乎表明所有边缘巢穴都无法养育幼崽，这主要是由于捕食。尽管如此，也许那些无法在栖息地中心占据一席之地的海鸥正好在边缘筑巢，而不是孤立地筑巢，对于像海鸥这样引人注目的鸟类来说，机会会更糟。")]

#html.p(id: "en-S016")[#text("It is perhaps worth digressing here to mention the temporal aspect of marginal predation. The “aggregation” in timing already alluded to for bats issuing from bat caves parallels the marked synchrony in breeding activities which is seen in most aggregations and which has been called the “Fraser Darling effect”. In explanation of this, Lack (1968) points out that late and early breeders in terns and the black-headed gull do worse in terms of young raised than those best-synchronized with the mass, and he implies that this is mainly due to predation. Individuals coming into breeding condition late or early may also have a problem in sexual selection-that of finding a mate. This point will be touched on later. There are similar influences of temporal selection for flowering plants.")]

#zh(id: "S016")[#text("这里也许值得题外话，提一下边缘掠夺的时间方面。已经提到的蝙蝠从蝙蝠洞出来的时间“聚集”与繁殖活动的显着同步性相似，这种同步性在大多数聚集中都可以看到，被称为“弗雷泽·达林效应”。在解释这一点时，拉克（Lack，1968）指出，燕鸥和黑头鸥的晚育和早育者在幼崽饲养方面比那些与群体同步最好的幼鸟表现更差，他暗示这主要是由于捕食造成的。较晚或较早进入繁殖状态的个体也可能在性选择方面存在问题，即寻找配偶的问题。这一点稍后会谈到。时间选择对开花植物也有类似的影响。")]

#html.p(id: "en-S017")[#text("The securing of a nest site in the middle of a colony area is certainly likely to be an achievement of protected position in a sense related to that explained in the story of the frogs, but in the relative immobility of such positions the case diverges somewhat from the initial theme. In all the")]

#zh(id: "S017")[#text("从与青蛙故事中所解释的相关的意义上来说，在殖民地区域中部确保巢穴的位置肯定可能是受保护位置的成就，但由于这些位置的相对固定性，该案例与最初的主题有些不同。在所有的")]

#html.p(id: "en-S018")[#text("I.% 20 foregoing examples, except perhaps that of the insect parasites of vertebrates, close analogy to that theme has also been lost through the assumption that the predator is likely to approach from outside the group. This is difficult to avoid.? When a predator habitually approaches from outside it is comparatively obvious how marginal pruning will at least maintain the centripetal instincts of the prey species. Whether predation could also initiate gregariousness in an originally non-gregarious species is another matter. As mentioned before, this will begin to seem likely if it can be shown that when predators tend to appear within a non-aggregated field of prey geometrical principles of self protection still orientate towards gregarious behaviour. So far I have only shown this for one highly artificial case: that of jumping organisms in a one dimensional universe. For the case in two dimensions a more realistic story can be given. The most realistic would, perhaps, take reindeer and warble flies as its subject animals, but in order to follow an interesting historical precedent, which has now to be mentioned, the animals chosen will be cattle and lions.")]

#zh(id: "S018")[#text("I.% 20 上述例子，除了脊椎动物的昆虫寄生虫之外，由于捕食者可能从群体外部接近的假设，与该主题的密切类比也已丢失。这是很难避免的。当捕食者习惯性地从外部接近时，相对明显的是，边缘捕杀至少会维持猎物物种的向心本能。捕食是否也会引发原本不群居的物种的群居性则是另一回事。如前所述，如果能够证明当捕食者倾向于出现在非聚集的猎物区域时，自我保护的几何原理仍然倾向于群居行为，那么这种情况似乎就有可能发生。到目前为止，我只展示了一个高度人为的案例：一维宇宙中跳跃的有机体。对于二维的情况，可以给出更现实的故事。最现实的也许是以驯鹿和莺蝇作为主题动物，但为了遵循一个有趣的历史先例（现在必须提及），选择的动物将是牛和狮子。")]

#html.p(id: "en-S019")[#text("In 1871 Francis Galton published in Macmillan’s Magazine an article entitled “Gregariousness in Cattle and in Men”. In it he outlined a theory of the evolution of gregarious behaviour based on his own observations of the behaviour of the half wild herds of cattle owned by the Damaras in South Africa. In spite of the characteristically forceful and persuasive style of his writing, Galton’s argument is not entirely clear and consistent. Some specific criticisms will be mentioned shortly. Nevertheless it does contain in embryo the idea of marginal predation as a force of natural selection leading to the evolution of gregarious behaviour. The main predators of the Damaraland cattle, according to Galton, were lions, and he states clearly that these did prefer to take the isolated and marginal beasts. The following passage shows sufficiently well his line of thought. After stating that the cattle are unamiable to one another and do not seem to have come together due to any “ordinary social desires”, he writes:")]

#zh(id: "S019")[#text("1871年，弗朗西斯·高尔顿在《麦克米伦杂志》上发表了一篇题为“牛和人的群居性”的文章。在书中，他根据自己对南非达马拉斯拥有的半野生牛群行为的观察，概述了群居行为进化的理论。尽管高尔顿的写作风格具有典型的有力和有说服力的风格，但他的论点并不完全清晰和一致。一些具体的批评将很快提到。尽管如此，它在胚胎中确实包含了边缘捕食的观念，作为自然选择的力量，导致群居行为的进化。根据高尔顿的说法，达马拉兰牛的主要掠食者是狮子，他明确指出，狮子确实更喜欢吃孤立的边缘动物。下面这段话充分说明了他的思路。在指出这些牛彼此不友好并且似乎不是由于任何“普通的社会愿望”而聚集在一起之后，他写道：")]

#html.p(id: "en-S020")[#text("“Yet although the ox has so little affection for, or individual interest in, his fellows, he cannot endure even a momentary severance from his herd. If he be separated from it by strategem or force, he exhibits every sign of mental agony; he strives with all his might to get back again and when he succeeds, he plunges into its middle, to bathe his whole body with the comfort of closest companionship.”")]

#zh(id: "S020")[#text("“然而，尽管牛对同伴没有多少感情或个人兴趣，但它却无法忍受与牛群短暂的分离。如果它被策略或武力与牛群分开，它就会表现出精神上的痛苦；它竭尽全力地想重新回来，当他成功时，它就会跳进牛群的中间，让自己的整个身体沐浴在最亲密的陪伴的舒适之中。”")]

#html.p(id: "en-S021")[#text("t Cannibalism in gregarious species raises different problems and may help to explain why the nests of gulls do not become very closely aggregated [see “the gull problem” in")]

#zh(id: "S021")[#text("群居物种的同类相食引发了不同的问题，可能有助于解释为什么海鸥的巢不会变得非常紧密地聚集在一起[参见《海鸥问题》")]

== 3. A Model of Predation in Two Dimensions / 3. 二维捕食模型

#html.p(id: "en-S022")[#text("Although as Galton implies, lions, like most other predators, usually attack from outside the herd, it is possible to imagine that in some circumstances a lion may remain hidden until the cattle are feeding on all sides of it. Consider therefore a herd grazing on a plain and suppose that its deep grass may conceal-anywhere-a lion. The cattle are unaware of danger until suddenly the lion is heard to roar. By reason of some peculiar imaginary quality the sound gives no hint of the whereabouts of the lion but it informs the cattle of danger. At any moment, at any point in the terrain the cattle are traversing, the lion may suddenly appear and attack the nearest cow.")]

#zh(id: "S022")[#text("尽管正如高尔顿所暗示的那样，狮子和大多数其他掠食者一样，通常从牛群外部发起攻击，但可以想象，在某些情况下，狮子可能会一直隐藏起来，直到牛在它的各个侧面进食。因此，考虑一下在平原上吃草的牛群，并假设其深厚的草丛可能在任何地方隐藏着狮子。牛群没有意识到危险，直到突然听到狮子吼叫。由于某种奇特的想象性质，这种声音并没有暗示狮子的行踪，但它告诉牛有危险。在牛所经过的地形上的任何时刻、任何地点，狮子都可能突然出现并攻击最近的牛。")]

#html.p(id: "en-S023")[#text("As in the case of the “frog” model, the rule that the predator attacks the nearest prey specifies a “domain of danger” for each individual. Each domain contains all points nearer to the owner of the domain than to any other individual. In the present case such domains are polygonal (Fig. 2). Each polygon is bounded by lines which bisect at right angles the lines which join the owner to certain neighbours; boundaries meet three at a point and an irregular tesselation of polygons covers the whole plane. On hearing the lion roar each beast will want to move in a way that will cause its polygonal domain to decrease. Not all domains can decrease at once of course: as in the case of the frogs, if some decrease others must grow larger; nevertheless, if one cow moves while others remain stationary the one moving can very definitely improve its position. Hence it can be assumed that inclinations to attempt some adaptive change of position will be established by natural selection. The optimal strategy of movement for any situation is far from obvious, and before discussing even certain better-than-nothing principles that are easily seen it will be a cautionary digression to consider what is already known about a particular and important case of such a tesselation of polygons, that in which the “centres” of polygons are scattered at random.")]

#zh(id: "S023")[#text("与“青蛙”模型的情况一样，捕食者攻击最近的猎物的规则为每个个体指定了一个“危险域”。每个域包含距离该域所有者比任何其他个人更近的所有点。在本例中，这些域是多边形的（图2）。每个多边形都由与连接所有者和某些邻居的线成直角平分的线界定；三个边界在一点处相交，不规则的多边形镶嵌覆盖了整个平面。当听到狮子的吼声时，每头野兽都会想要以一种会导致其多边形域减小的方式移动。当然，并非所有领域都会立即减少：就像青蛙的情况一样，如果某些领域减少，其他领域就必须变大；然而，如果一头牛移动而其他牛保持静止，则移动的一头牛肯定可以改善其位置。因此，可以假设，尝试某种适应性改变位置的倾向将通过自然选择而建立。任何情况下的最佳移动策略都远非显而易见，在讨论某些聊胜于无的原则之前，考虑一下这种多边形镶嵌的特定且重要的情况（其中多边形的“中心”是随机分散的）的已知情况将是一个谨慎的题外话。")]

#html.p(id: "en-S024")[#text("Patterns of a more concrete nature which are closely analogous to the tesselation defined certainly exist in nature. In two dimensions they may be seen in the patterns formed by encrusting lichens on rocks, and in the cross-sectional patterns of cracks in columnar basalt. The corresponding pattern in three dimensions, consisting of polyhedra, is closely imitated in the crystal grains of some metals and other materials formed by solidification of liquids. The problem of the statistical description of the pattern in the case where centres are distributed at random was first attacked with reference to the grain structure of metals (Evans, 1945). More recently the N-dimensional analogue has been studied by E. N. Gilbert (1962) on the incentive of a problem arising in communication science. Yet in spite of great expertise many simple facts about even the two-dimensional case remain")]

#zh(id: "S024")[#text("自然界中肯定存在与定义的镶嵌密切相似的更具体性质的图案。在二维中，它们可以在岩石上的地衣结壳形成的图案中以及柱状玄武岩裂缝的横截面图案中看到。由液体凝固形成的一些金属和其他材料的晶粒紧密地模仿了由多面体组成的三维相应图案。在中心随机分布的情况下，模式的统计描述问题首先参考金属的晶粒结构来解决（Evans，1945）。最近，E. N. Gilbert (1962) 对 N 维类似物进行了研究，以探讨通信科学中出现的问题的诱因。然而，尽管拥有丰富的专业知识，但即使是二维情况，许多简单的事实仍然存在")]

#html.figure(id: "F004", class: "essay-paper-figure")[
  #image("assets/figure-04.png")
]

#html.p(id: "en-C002", class: "essay-original-caption")[#text("FIG. 2. Domains of danger for a randomly dispersed prey population when a hidden predator will attack the nearest animal. Thin arrowed lines indicate the nearest neighbour of each prey. Thicker arrowed lines show supposed movements of particular prey. Position of prey is given a lower case letter and the domain obtained from each position is given the corresponding upper case letter. The pattern underlining the domain letter corresponds to the pattern used to indicate the boundary of the domain in question. Dashed lines are used for the boundaries of domains that come into existence after the first movement. Approach to a nearest neighbour usually diminishes the domain of danger (as a + b), but not always (as y + z). On reaching a neighbour the domain may, in theory, be minimized by moving round to a particular side (as b + c). The inset diagram shows geometrical algorithms for minimum domains attainable by a (on reaching c), and by y. In the case of y the minimum domain is equal to the triangle of neighbours and is obtained from the orthocentre of that triangle.")]

#zh(id: "C002")[#text("如图。 2. 当隐藏的捕食者攻击最近的动物时，随机分散的猎物种群的危险域。细箭头线表示每个猎物的最近邻居。较粗的箭头线显示了特定猎物的假定运动。猎物的位置用小写字母表示，从每个位置获得的域用相应的大写字母表示。域字母下划线的模式对应于用于指示相关域边界的模式。虚线用于第一次运动后出现的域的边界。接近最近邻居通常会缩小危险范围（如 a + b），但并非总是如此（如 y + z）。理论上，在到达邻居时，可以通过移动到特定一侧（如 b + c）来最小化域。插图显示了 a（到达 c 时）和 y 可达到的最小域的几何算法。在 y 的情况下，最小域等于邻居的三角形，并且是从该三角形的垂心获得的。")]

#html.p(id: "en-S025")[#text("unknown. The distribution of the angles of the polygons is known (J. L. Meijering, personal communication); something is known of the lengths of their sides, and Gilbert has found the variance of their areas.? Nothing, apart from the fairly obvious value of six for the mean, is known of the numbers of sides. Since a biologist might be interested to know whether, in the ideal territory system of these polygons, six neighbours is the most likely number, or whether five is more likely than seven, some data gathered from plots of random numbers is given in Table 1. TABLE 1 Distribution of the number of sides of 376 polygons constructed from random number plots")]

#zh(id: "S025")[#text("未知。多边形的角度分布是已知的（J. L. Meijering，个人通讯）； ？已知它们边长，吉尔伯特发现了它们面积的差异。？除了相当明显的平均值六之外，我们对边数一无所知。由于生物学家可能有兴趣知道，在这些多边形的理想领土系统中，六个邻居是否是最可能的数字，或者五个邻居是否比七个更有可能，因此表 1 中给出了从随机数图中收集的一些数据。 表 1 从随机数图构建的 376 个多边形的边数分布")]

#html.figure(id: "T001", class: "essay-paper-figure")[
  #image("assets/table-05.png")
]

#zh(id: "T001")[#text("边数；观察到的数量；观察总数。")]

#html.p(id: "en-C003", class: "essay-original-caption")[#text("Data for 100 of these polygons were received from E. N. Gilbert. The rarity of triangles indicates that the sample area chosen for Fig. 2 is not quite typical.")]

#zh(id: "C003")[#text("其中 100 个多边形的数据来自 E. N. Gilbert。三角形的稀有性表明为图 2 选择的样本区域并不十分典型。")]

#html.p(id: "en-S026")[#text("After glancing at Gilbert’s paper a non-mathematical biologist may well despair of finding a theory of idealself-protective movement for the random cattle. Nevertheless experimentation with ruler and compasses and one small evasion quickly reveal a plausible working principle. As a preliminary it may be pointed out that the problem differs radically from the linear problem in that domains of danger change continuously in size with movements of their owner. (In the linear case no change takes place until an individual actually passes his neighbour; this was the reason for choosing organisms that jump.) Now suppose that one cow alone has sensed the presence of the lion and is hastily moving through an otherwise motionless herd. In most circumstances such a cow will diminish its domain of anger by approaching its nearest neighbour. A direct approach can seldom be the path it would choose if it requires that every step should bring the maximum decrease of danger, and when the nearest neighbour is a rather isolated individual it may even happen that a domain increases during approach to a nearest neighbour (Fig. 2, y + z). Such increases will tend to be associated with polygons with very low side number. When an individual is enclosed in a ring of others and consequently owns a many-sided domain, decrease in area is almost inevitable (Fig. 2, a -+ b). Since the average number of sides is six and triangles are rare (Table l), it must be a generally useful rule for a cow to approach its nearest t Recently R. E. Miles (1970) has greatly extended analysis of this case (Mark &~ci. 6, 85) (footnote added in proof).")]

#zh(id: "S026")[#text("在浏览了吉尔伯特的论文后，非数学生物学家可能会对为随机牛找到理想的自我保护运动理论感到绝望。尽管如此，用尺子和圆规进行的实验以及一次小小的回避很快就揭示了一个看似合理的工作原理。首先可以指出，该问题与线性问题截然不同，因为危险域的大小随着其所有者的移动而不断变化。 （在线性情况下，只有在一个个体真正经过他的邻居之前，才会发生变化；这就是选择跳跃生物的原因。）现在假设一头牛独自感知到狮子的存在，并匆忙穿过原本一动不动的牛群。在大多数情况下，这样的牛会通过接近最近的邻居来减少其愤怒范围。如果要求每一步都最大限度地减少危险，那么直接接近很少会成为它所选择的路径，并且当最近邻居是一个相当孤立的个体时，甚至可能会出现在接近最近邻居的过程中域增加的情况（图2，y+z）。这种增加往往与边数非常低的多边形相关。当一个个体被包围在其他人的环中并因此拥有多边域时，面积的减小几乎是不可避免的（图2，a - + b）。由于平均边数为 6 并且三角形很少见（表 l），因此对于奶牛来说，接近其最近的 t 一定是一个普遍有用的规则。最近，R. E. Miles (1970) 对这种情况进行了极大的扩展分析 (Mark &~ci. 6, 85)（在证明中添加了脚注）。")]

#html.p(id: "en-S027")[#text("neighbour. This is a rule for which natural selection could easily build the necessary instincts. Behaviour in accord with it has been reported in sheep (Scott, 1945). The evasion, then, is to imagine that these imaginary cattle are too slow-witted to do anything better. Most readers will agree, I hope, that there is no need to call them stupid on this account.")]

#zh(id: "S027")[#text("邻居。自然选择可以很容易地为这条规则建立必要的本能。据报道，绵羊也有与之相符的行为（Scott，1945）。那么，逃避就是想象这些想象中的牛太迟钝，无法做任何更好的事情。我希望大多数读者都会同意，没有必要因此而称他们为愚蠢。")]

#html.p(id: "en-S028")[#text("If the rest of the herd remains stationary and the alarmed cow reaches its nearest neighbour it will usually further decrease its domain of danger by moving round to a side that gives it a minimal “corner” of the neighbour’s now enlarged domain (Fig. 2, b -+ c; left inset diagram shows the principle for finding such a minimal “corner” domain. In this position the cow of the story may be supposed to reach equilibrium; it is some sort of equivalent, albeit not a close one, of the stable non-jump positions that sometimes occur with the frogs. Even more than with the stable positions of the frogs, however, the stable positions of this model must be almost impossible to attain. As in the case of the frogs this is seen as soon as we imagine that all the other are moving and have similar aims in view. COWS Nearest-neighbour relationships connect up points into groups (Fig. 2). Every group has somewhere in it a “reflexive pair”; that is, a pair for which each is the nearest neighbour of the other. A formula for the frequency of membership of reflexive pairs when the points are randomly dispersed has been derived by Clark & Evans (1955). It is 6?r/(&r+J27). Halving and inverting this expression gives us the average size of groups as 3.218. No further facts are known mathematically about the relative frequencies of different sizes of groups, but a summary of the forms and sizes found in the random number plots is given in Table 2.")]

#zh(id: "S028")[#text("如果牛群的其余部分保持静止，而受惊的牛到达最近的邻居，它通常会通过移动到一侧来进一步减少其危险范围，从而为邻居现在扩大的区域提供一个最小的“角落”（图2，b - + c；左插图显示了找到这样一个最小“角落”区域的原理。在这个位置，故事中的牛可能会达到平衡；它是马厩的某种等价物，尽管不是很接近。然而，与青蛙的稳定位置相比，这种情况几乎是不可能实现的，只要我们想象所有其他青蛙都在移动并且具有相似的目标，每个组中都有一个“自反对”。 Clark & Evans (1955) 推导了点随机分散时的自反对的隶属频率公式，该公式为 6?r/(&r+J27)。将该表达式减半并反转后，我们可以得到组的平均大小为 3.218。从数学角度看，我们无法得知有关不同大小组的相对频率的更多事实，但表 2 给出了随机数图中的形式和大小的摘要。")]

#html.p(id: "en-S029")[#text("Clearly, if randomly dispersed cattle condense according to the statistical pattern indicated in Table 2, the groups so formed can hardly be described as herds. Nevertheless there is undoubtedly a gregarious tendency of a kind, and once such primary groups have formed the cattle in each group will see a common advantage in moving through the field of groups using the same principles as before. Thus an indefinite series of such condensations will take place and eventually large herds will appear. Condensation is not prevented by having the points initially more evenly spaced than in the random dispersion. For example, when the points are initially in some lattice formation the inherent instability of the system is actually easier to see than it is for the random dispersion: every point, if moving alone, can definitely diminish its domain of danger by approaching any one of its equidistant neighbours. Thus even for the most unpromising initial conditions it remains evident that predation should lead to the evolution of gregarious behaviour.")]

#zh(id: "S029")[#text("显然，如果随机分散的牛按照表2所示的统计模式聚集在一起，那么这样形成的群体就很难被描述为牛群。尽管如此，毫无疑问存在着一种群居倾向，一旦这样的主要群体形成，每个群体中的牛就会看到使用与以前相同的原则在群体领域中移动的共同优势。因此，将发生无限系列的此类凝聚，最终将出现大群。最初使点比随机分散中的点间隔更均匀并不能防止凝结。例如，当这些点最初处于某种晶格结构时，系统固有的不稳定性实际上比随机分散更容易看到：每个点如果单独移动，肯定可以通过接近任何一个等距邻居来缩小其危险范围。因此，即使在最没有希望的初始条件下，捕食仍会导致群居行为的进化，这一点仍然很明显。")]

#html.p(id: "en-S030")[#text("No story even as poorly realistic as the foregoing can be given for the")]

#zh(id: "S030")[#text("没有任何故事，即使是像上述那样不切实际的故事")]

#html.figure(id: "T002", class: "essay-paper-figure")[
  #image("assets/table-06.png")
]

#zh(id: "T002")[#text("组内个体数；发现的案例数；发现的构型；组内个体平均数：实测值、预期值。")]

#html.p(id: "en-C004", class: "essay-original-caption")[#text("The nearest neighbour relation allocates points of a random dispersion to groups (see arrowed lines on Fig. 2). Here the configurations found in 121 groups formed by 376 points are recorded together with their frequencies of occurrence. Double connecting lines indicate the reflexive nearest neighbour relationship.")]

#zh(id: "C004")[#text("最近邻关系将随机分散的点分配给组（参见图 2 上的箭头线）。这里记录了由 376 个点组成的 121 个组中发现的构型及其出现频率。双连接线表示自反最近邻关系。")]

#html.p(id: "en-S031")[#text("case of predation in three dimensions. In the air and in water there is still less cover in which the predator can hide. If there were a hiding place, however, for what it is worth the argument can be repeated almost exactly and we arrive at 3+ for the mean size of primary groups. For celestial cattle in a space of infinitely many dimensions the mean group size attains only to 4.t")]

#zh(id: "S031")[#text("三维掠夺的情况。在空气和水中，捕食者可以隐藏的掩护物仍然较少。然而，如果有一个隐藏的地方，无论其价值如何，论证都可以几乎完全重复，并且我们得出主要群体的平均规模为 3+。对于无限多维空间中的天牛来说，平均群体大小仅达到 4.t")]

#html.p(id: "en-S032")[#text("Whether or not marginal predation is, as I believe it to be, a common primary cause of the evolution of gregariousness, it is surprising that the idea of such a cause has received so little attention from biologists. The reason for the neglect of Galton’s views cannot lie in the non-scientific nature of the journal in which it was originally published. Galton repeated them in his book Inquiries into Human Faculty (1883), and this is one of")]

#zh(id: "S032")[#text("无论边缘捕食是否如我所认为的那样，是群居性进化的一个常见的主要原因，令人惊讶的是，这样一个原因的想法很少受到生物学家的关注。高尔顿观点被忽视的原因不能在于最初发表该观点的期刊的非科学性。高尔顿在他的《人类能力的探究》（1883）一书中重复了这些内容，这是其中之一")]

#html.p(id: "en-S033")[#text("? The general formula, where n is the number of dimensions, is his best known works. Yet both the hints of the present hypothesis in writings on the schooling of fishes and the admirable study and discussion of this hypothesis by G. C. Williams (1964) were completely independent of Galton’s publications. Galton himself is certainly largely to blame for this. With one exception he did not relate his idea to species other than cattle and sheep, and the one exception was man. Something of the tenor of his views on the manifestations of gregariousness in man may be gathered from the fact that the relevant passage in the book mentioned above is headed: “On gregarious and slavish instincts”. Needless to say his analogy between human and bovine behaviour now seems somewhat naive. His views remain, as always, interesting and evocative, but their dogmatic and moralizing tone and their obvious connection with their author’s widely distrusted line on eugenics can be imagined to have scared off many potentially interested zoologists. Another probable reason for the neglect of Galton’s idea is that he himself presented it mixed up with another really quite separate idea which he treated as if it were simply another aspect of the same thing. This was that every cow, whether marginal or interior, benefited by being part of a herd, and that therefore herding was beneficial to the species. His supporting points are undoubtedly forcible; he mentions mutual warning and the idea that by forming at bay in outward-facing bands the cattle can present a really formidable defence against the lions. However, whether or not the cattle actually do, in the last resort, overcome their centripetal inclination and turn to face the predator (as smaller bands of “musk ox” certainly do), these points raise a different issue, as do the mass attacks on predators by gregarious nesting birds. My models certainly give no indication that such mutualistic defence is a necessary part of gregarious behaviour. Moreover, mutual defence and warning can hardly be described as “slavish” behaviour and so seem not to be covered by Galton’s heading. There is no doubt, of course, that mutual warning and occasional unselfish defence of others are sometimes shown by gregarious mammals and birds, but where such actions occur they are probably connected on the one hand with the smallness of the risk taken and, on the other, with the closeness of the genetical relationship of the animals benefited (Hamilton, 1963). With the musk ox, for example, the bands are small and clearly based on close family relationships. Sheep and cattle also take risks in defending their young (as Galton pointed out), but this is based on recognition of their own offspring. Apart from the forced circumstances, and the unnatural dispositions engendered by domestication, females usually do not associate with, still less defend, young which are not their own (Williams, 1966). The ability to recognize particular individuals of the same species is highly developed in mammals and birds and there is no difficulty either practical or theoretical in supposing that the mutualistic behaviour of the adult musk oxen, for instance, is an evolutionary development from the altruism involved in parental care. Positive social relations between members of family groups probably exist submerged in most manifestations of mass gregariousness in animals higher than fish. For example the flock of sheep driven by a shepherd owes its compactness and apparent homogeneity to the presence of the sheep dogs: when it is left undisturbed on the mountain it arranges itself into a loosely clustered and loosely territorial system. The clusters are usually based on kinship and the sheep of a cluster are antagonistic to any strange sheep that attempts to feed on their ground (Hunter, 1964). It accords well with the present theory that the breeds of sheep that are most readily driven into large flocks are those which derive from the Merino breed of Spain (Darling, 1937) which is an area where, until very recently, predation by wolves was common. Galton likewise gave the relaxation of predation as the reason for European cattle being very much less strongly gregarious than the cattle he observed in Africa. He noted that the centripetal inclinations evolved through predation would be opposed continually by the need to find ungrazed pasture, so that when predation is relaxed gregarious instincts would be selected against. This point has also been made by Williams.")]

#zh(id: "S033")[#text("？通式（其中 n 是维数）是他最著名的著作。然而，有关鱼类成群的著作中现有假说的暗示，以及 G. C. Williams (1964) 对这一假说的令人钦佩的研究和讨论，都完全独立于高尔顿的出版物。高尔顿本人肯定对此负有主要责任。除了一个例外，他没有将他的想法与牛和羊以外的物种联系起来，唯一的例外是人类。他关于人类群居性表现的观点的主旨可以从上述书中相关段落的标题中看出：“论群居性和奴性本能”。不用说，他对人类和牛行为的类比现在看来有些幼稚。他的观点一如既往地有趣且令人回味，但其教条和说教的语气以及与作者广泛不信任的优生学路线的明显联系可以想象吓跑了许多潜在感兴趣的动物学家。忽视高尔顿的想法的另一个可能原因是，他本人将其与另一个完全独立的想法混合在一起提出，他将其视为同一事物的另一个方面。也就是说，每头牛，无论是边缘还是内部，都因成为牛群的一部分而受益，因此放牧对该物种有利。他的支撑点无疑是有力的；他提到了相互警告以及这样的想法：通过形成面向外的群体，牛可以对狮子形成真正强大的防御。然而，无论牛最终是否真的克服向心倾向并转向面对捕食者（就像较小的“麝牛”群体肯定会做的那样），这些点都提出了不同的问题，就像群居筑巢的鸟类对捕食者的大规模攻击一样。我的模型当然没有表明这种互惠防御是群居行为的必要组成部分。而且，相互防御和警告很难说是“奴性”行为，因此似乎不在高尔顿的标题之内。当然，毫无疑问，群居的哺乳动物和鸟类有时会表现出相互警告和偶尔无私的保护他人，但这种行为发生时，一方面可能与所冒风险较小有关，另一方面与受益动物的遗传关系密切有关（Hamilton，1963）。例如，麝香牛的族群很小，而且显然是建立在密切的家庭关系的基础上的。羊和牛也会冒​​着保护后代的风险（正如高尔顿指出的），但这是基于对自己后代的认可。除了被迫的环​​境和驯化所产生的不自然的性情之外，女性通常不与其他动物交往，更不用说保护它们了。不属于自己的年轻人（Williams，1966）。哺乳动物和鸟类具有高度发达的识别同一物种特定个体的能力，假设成年麝牛的互惠行为是父母照顾中的利他主义的进化发展，无论在实践还是理论上都没有困难。家庭群体成员之间积极的社会关系可能隐藏在比鱼类高等动物的集体群居性的大多数表现中。例如，牧羊人驱赶的羊群由于牧羊犬的存在而具有紧凑性和明显的同​​质性：当它在山上不受干扰时，它会将自己排列成松散的集群和松散的领地系统。这些羊群通常是基于亲缘关系的，羊群中的羊对任何试图在其土地上进食的陌生羊都是敌对的（Hunter，1964）。这与目前的理论非常一致，即最容易被驱赶到大羊群中的绵羊品种是源自西班牙美利奴品种的绵羊品种（Darling，1937），直到最近，该地区还经常被狼捕食。高尔顿同样认为，捕食的放松是欧洲牛群居性远不如他在非洲观察到的牛的原因。他指出，通过捕食进化而来的向心倾向将不断受到寻找未放牧牧场的需要的反对，因此，当捕食放松时，群居本能将被选择对抗。威廉姆斯也指出了这一点。")]

#html.figure(id: "E001", class: "essay-equation")[
  #image("assets/equation-07.png")
]

#html.p(id: "en-S034")[#text("Most writers on the subject of animal aggregation seem to have believed that the evolution of gregarious behaviour must be based on some advantage to the aggregation as a whole. Many well known biologists have subscribed, outspokenly or by implication, to this view. At the same time some, for example Hesse et al. (1937), Fisher (1953) and Lorenz (1966), have admitted that the nature of the group advantage remains obscure in many cases. On the hypothesis of gregarious behaviour presented here the apparent absence of a group benefit is no cause for surprise. On the contrary, the hypothesis suggests that the evolution of the gregarious tendency may go on even though the result is a considerable lowering of the overall mean fitness. At the end of our one-dimensional fairy tale, it will be remembered, only the snake lives happily, taking his meal at leisure from the scrambling heaps of frogs which the mere thought of his existence has brought into being. The cases of predators feeding on apparently helpless balls of fish seem parallel to this phantasy : here gregariousness seems much more to the advantage of the species of the predator than to that of the prey. Certain predators of fish appear to have evolved adaptations for exploiting the schooling tendencies of their prey. These cases are not only unfavourable to the hypothesis of a group advantage in schooling but also somewhat unfavourable to the present hypothesis, since it begins to seem that there must be an advantage to fish which do not join the school. The thresher shark is said to use its much elongated tail to round up fish into easily eaten schools (Williams, 1964).")]

#zh(id: "S034")[#text("大多数关于动物聚集主题的作者似乎都认为，群居行为的进化必须基于对整个聚集的某些优势。许多著名的生物学家都直接或暗示地赞同这一观点。与此同时，一些人，例如黑塞等人。 (1937)、Fisher (1953) 和 Lorenz (1966) 都承认，群体优势的本质在许多情况下仍然是模糊的。根据这里提出的群居行为假设，明显缺乏群体利益并不令人惊讶。相反，该假设表明，即使结果是总体平均适应度显着降低，群居倾向的进化也可能会继续下去。在我们的一维童话故事的结尾，人们会记得，只有蛇幸福地生活着，悠闲地从青蛙堆中进食，而这些青蛙只是因为想到了它的存在而产生的。捕食者以明显无助的鱼球为食的例子似乎与这种幻想相似：在这里，群居性似乎对捕食者的物种比对猎物的物种更有好处。某些鱼类的捕食者似乎已经进化出适应能力，以利用猎物的成群倾向。这些情况不仅不利于鱼群教育中群体优势的假设，而且对目前的假设也有些不利，因为看起来不加入鱼群的鱼一定具有优势。据说长尾鲨利用其细长的尾巴将鱼聚集成容易被吃掉的鱼群（Williams，1964）。")]

#html.p(id: "en-S035")[#text("Even worse, the swordfish is recorded as feeding on schools by first immobilizing large numbers with blows from its sharp-edged sword. This may be its usual method of feeding, and the sawflsh may use its weapon similarly. Such predators presumably do best by striking through the middle of a school; lone fish might fail to attract them. It is obvious, however, that such cases should not be assessed on the assumption that a particular predator is the only one (Bullis, 1960). At the time of attack by a swordfish there may be other important predators round about that are still concentrating on the isolated and peripheral fish. In the case of locusts the occurrence of such contrary influences from predation is recorded (Hudleston, 1957) : large bird predators (ravens and hornbills) attacking bands of hoppers of the desert locust did tend to disperse the bands, and to decimate their central members, by settling in their midst, but at the same time smaller birds (chats and warblers) captured only marginal hoppers and stragglers.")]

#zh(id: "S035")[#text("更糟糕的是，据记录，旗鱼以鱼群为食，首先用锋利的剑击打大量鱼群，使其无法动弹。这可能是它通常的进食方式，锯鱼也可能类似地使用它的武器。这些掠食者大概最擅长袭击学校的中间。孤独的鱼可能无法吸引它们。然而，显然，不应假设特定的捕食者是唯一的捕食者（Bullis，1960）来评估此类情况。当剑鱼攻击时，周围可能还有其他重要的捕食者，它们仍然集中在孤立和外围的鱼类上。就蝗虫而言，捕食造成的这种相反影响的发生是有记录的（Hudleston，1957）：攻击沙漠蝗虫群的大型鸟类捕食者（渡鸦和犀鸟）确实往往会驱散蝗群，并通过定居在它们中间来消灭它们的中心成员，但同时较小的鸟类（鹬和莺）仅捕获边缘的跳跃者和掉队者。")]

#html.p(id: "en-S036")[#text("Adaptations of the predator to exploit the gregariousness of its prey certainly suggests the possibility of a changeover to a disaggregating phase of selection. In terms of the earlier story, if the snake evolves such a lazy preference for taking its prey from a heap that it comes to overlook a nearer lone frog, then it may come to be the mutant gregariphobe which survives best to propagate its kind. There are in fact many examples of species which are gregarious in only part of their range or their life cycle and possibly this may reflect the differing influences of different predators.")]

#zh(id: "S036")[#text("捕食者利用猎物的群居性进行的适应无疑表明了选择的分解阶段的可能性。就之前的故事而言，如果蛇进化出了一种懒惰的偏好，喜欢从一堆猎物中获取猎物，以至于忽略了更近的孤独青蛙，那么它可能会成为变异的恐鸟症，最能生存下来并繁殖其同类。事实上，有许多物种的例子仅在其范围或生命周期的一部分内是群居的，这可能反映了不同捕食者的不同影响。")]

#html.p(id: "en-S037")[#text("A surprising number of discussions of animal aggregation have mentioned the occurrence of marginal predation and yet shown apparently no appreciation of its possible evolutionary significance. Whether marginal predation or similarly orientated pressure of selection on individuals is sufficiently powerful to account for the gregariousness observed in any particular case cannot be decided by any already existing body of data. Nevertheless it can be claimed that for none of the cases so far discussed does the data exclude the possibility. It can also be claimed that all the rival theories based on the idea of “group selection” are theoretically insecure. Consider for example the theory of Wynne-Edwards (1962) which, from this basis, attempts to bring many facts of animal aggregation under a common explanation. This theory suggests that aggregations serve to make individuals aware of the current level of population density and that this awareness reacts on reproductive performance in a way that holds off the possibility of a disastrous crash due to over-exploitation of the food supply or other limited resources. Except in cases where groups are exclusive and mutually competitive for territory it is very difficult to see how there can be positive selection of any tendency by an individual to reproduce less effectively than it is able (Hamilton, 1971). Wynne-Edwards’s cases of massive aggregations, even those having a kin-based substructure as in the gregarious ungulates, are unlikely candidates for the class of exceptions. The alternative theory supported here has no parallel difficulty as to the underlying processes of selection since it can rest firmly on the theory of genetical natural selection.")]

#zh(id: "S037")[#text("数量惊人的关于动物聚集的讨论都提到了边缘捕食的发生，但显然没有意识到其可能的进化意义。边际掠夺或类似的个体选择压力是否足以解释在任何特定情况下观察到的群居性，都不能由任何现有的数据来决定。尽管如此，可以说，对于迄今为止讨论的所有案例，数据均未排除这种可能性。也可以说，所有基于“群体选择”思想的竞争理论在理论上都是不安全的。例如，考虑 Wynne-Edwards (1962) 的理论，该理论在此基础上试图将动物聚集的许多事实置于共同的解释之下。该理论表明，聚集有助于使个体意识到当前的人口密度水平，并且这种意识对繁殖性能产生反应，从而阻止由于过度开发粮食供应或其他有限资源而导致灾难性崩溃的可能性。除非群体是排他性的并且相互竞争领土的情况，否则很难看出如何能够积极选择个体的繁殖效率低于其能力的任何倾向（Hamilton，1971）。韦恩-爱德华兹的大规模聚集案例，即使是那些具有基于亲属关系的亚结构（如群居有蹄类动物）的案例，也不太可能属于例外类别。这里支持的替代理论在选择的基本过程方面没有类似的困难，因为它可以牢固地建立在遗传自然选择理论的基础上。")]

#html.p(id: "en-S038")[#text("Certain other versions of the idea of a group benefit, unlike the Wynne- Edwards theory, do not require the concept of self-disciplined restraint by individuals. With such versions, statements that aggregation has evolved because it aids the survival of the species may be treated as merely errors of expression, in which a possibly genuine effect is given the status of a cause. The factor of communal alertness, for instance, may really make life more difficult for a predator and safer for a gregarious prey, especially if the predator is one which relies on stealth rather than speed. In Galton’s perhaps over-persuasive words,")]

#zh(id: "S038")[#text("与韦恩-爱德华兹理论不同，群体利益理念的某些其他版本不需要个人自律约束的概念。在这样的版本中，关于聚集之所以进化是因为它有助于物种生存的说法可能被视为纯粹的表达错误，其中可能真正的结果被赋予了原因的地位。例如，群体警觉性的因素确实可能使捕食者的生活变得更加困难，而对于群居的猎物来说则更加安全，特别是如果捕食者是依靠隐秘而不是速度的捕食者的话。用高尔顿也许过于有说服力的话来说，")]

#html.p(id: "en-S039")[#text("“To live gregariously is to become a fibre in a vast sentient web overspreading many acres; it is to become the possessor of faculties always awake, of eyes that see in all directions, of ears and nostrils that explore a broad belt of air; it is to become the occupier of every bit of vantage ground whence the approach of a lurking enemy might be overlooked.”")]

#zh(id: "S039")[#text("“群居生活就是成为覆盖数英亩的巨大感知网络中的一根纤维；就是成为拥有永远清醒的能力、拥有观察四面八方的眼睛、拥有探索广阔空气带的耳朵和鼻孔的拥有者；就是成为每一个有利位置的占有者，从那里可以忽视潜伏敌人的接近。”")]

#html.p(id: "en-S040")[#text("But there is of course nothing in the least altruistic in keeping alert for signs of nervousness in companions as well as for signs of the predator itself, and there is, correspondingly, no difficulty in explaining how gregariousness on this basis could be evolved.")]

#zh(id: "S040")[#text("但是，对同伴的紧张迹象以及捕食者本身的迹象保持警惕，当然没有丝毫利他主义的成分，相应地，解释在此基础上的群居性是如何进化出来的也没有困难。")]

#html.p(id: "en-S041")[#text("Returning to the more interesting and controversial postulate of a population regulatory function for mass aggregation, consider, as a point of detailed criticism, the problem presented by aggregations in which several species are mixed. All the main classes of aggregation that have so far been mentioned -fish schools, bird flocks (both mobile and nesting) and grazing herdsprovide numerous examples of species mixture. The species involved may be as widely related as ostriches and antelopes (Hesse et al., 1937). If it is difficult to see how the supposed group selection can work within a species it is certainly even more difficult when the groups are mixed. On the other hand the theory that gregariousness is essentially due to the need for cover finds no difficulty over this point provided that the species which mix have at least one important predator in common. None of the vertebrate predators that have been mentioned as possible agents for the moulding of gregarious inclinations in their prey seem so specialized in their hunting as to make it improbable that individuals of one prey species could expect to gain some protection by immersing themselves in an aggregation of another species.")]

#zh(id: "S041")[#text("回到更有趣和有争议的大规模聚集的种群调节功能的假设，作为详细批评的一点，考虑由多个物种混合的聚集所带来的问题。迄今为止提到的所有主要聚集类别——鱼群、鸟群（包括移动的和筑巢的）和牧群提供了许多物种混合的例子。所涉及的物种可能与鸵鸟和羚羊一样广泛相关（Hesse et al., 1937）。如果很难看出所谓的群体选择如何在一个物种内发挥作用，那么当群体混合时肯定会更加困难。另一方面，只要混合的物种至少有一个共同的重要捕食者，群居性本质上是由于需要掩护的理论在这一点上就没有困难。被认为是塑造猎物群居倾向的可能媒介的脊椎动物捕食者似乎都没有如此专业化地捕猎，以至于一个猎物物种的个体不可能期望通过将自己融入到另一个物种的聚集中来获得某种保护。")]

#html.p(id: "en-S042")[#text("Perhaps most of the examples of mixed aggregation lie outside the class for which Wynne-Edwards and his supporters would claim a population regulatory function. The examples which have been cited in support of the theory are, in general, more directly concerned with reproduction. Apart from the case of nest aggregations, which has been discussed, there remain Wynne- Edwards’s numerous citations of nuptial gatherings. With these the case for the effectiveness of marginal predation is admittedly weaker. Marginal predation seems somewhat less likely on general grounds and there is little evidence. However, there are other ways in which selection is likely to favour individuals which are in the nuptial gathering (or at least on its margin) over those that are isolated. Such selection may be sexual; it may work through differences in the chances of obtaining a mate. As one example, consider the swarms of midges that are so common in damp, still, vegetated places in summer. Many species of nematocerous flies have the habit of forming such swarms. Each swarm usually consists of males of a single species and tends to hover in a lixed spot, often near to some conspicuous object. Females come to the swarm and on arrival each is seized by a male. Passing over possible stages in the initiation of such habits, it is at least clear that as soon as proximity to the swarm itself becomes a key to the female’s further co-operation in copulation there is likely to be little chance of mating for the male which does not join the swarm. In such a case the optimal position for a male is probably, not, as it is under predation, at the centre of the throng, and considering how males might endeavour to spend the maximum time in relatively favoured positions, downwind or upwind, above or below, possible explanations for the dancelike motion of such swarms become apparent.")]

#zh(id: "S042")[#text("也许大多数混合聚合的例子都不属于韦恩-爱德华兹及其支持者所声称的人口调节功能的范畴。一般来说，为支持该理论而引用的例子更直接地涉及繁殖。除了已经讨论过的巢聚集的例子之外，韦恩-爱德华兹仍然对婚姻聚会进行了大量的引用。在这些情况下，边际掠夺的有效性的论据无疑较弱。从一般情况来看，边缘掠夺的可能性似乎不大，而且几乎没有证据。然而，还有其他一些方式，选择可能有利于那些参加婚礼聚会（或至少在其边缘）的个体，而不是那些孤立的个体。这种选择可能是性的；它可能通过获得配偶的机会差异来发挥作用。举个例子，想想夏季潮湿、静止、植被茂盛的地方常见的成群蠓虫。许多种类的线虫蝇都有形成这样的群体的习惯。每个群体通常由单一物种的雄性组成，并且倾向于盘旋在固定位置，通常靠近一些显眼的物体。雌性来到蜂群中，到达后每只都被雄性抓住。忽略这些习惯开始的可能阶段，至少可以清楚的是，一旦接近群体本身成为雌性在交配中进一步合作的关键，那么不加入群体的雄性交配的机会就很小了。在这种情况下，雄性的最佳位置可能不是在被捕食时处于人群的中心，并且考虑到雄性如何努力将最大时间花在相对有利的位置，顺风或逆风，上方或下方，对此类群体的舞蹈般运动的可能解释变得显而易见。")]

#html.p(id: "en-S043")[#text("I wish to thank Dr I. Vine for the stimulus to publish this paper: his paper (J. theor. Biol. 30, 405), treating the influence of predation from a different point of view and showing one way in which gregariousness may be beneficial to the group as a whole, was sent to me in manuscript.")]

#zh(id: "S043")[#text("我要感谢 I. Vine 博士促使我发表这篇论文：他的论文 (J. theor. Biol. 30, 405) 从不同的角度处理了掠夺的影响，并展示了群居性可能对整个群体有利的一种方式，该论文以手稿形式发送给了我。")]

== References / 参考文献

#html.p(id: "en-R001")[#text("Ausn~, ELE. (1939).In British Bloodsucking Flies. (F. W. Edwards, H. Oiroyd & J. Smart, eds.), pp. 149-152. London: British Museum.")]

#zh(id: "R001")[#text("奥斯恩〜，ELE。 (1939)。《英国吸血蝇》。 （F. W. Edwards、H. Oiroyd 和 J. Smart 编辑），第 149-152 页。伦敦：大英博物馆。")]

#html.p(id: "en-R002")[#text("BAERBNDS,G. P. & BAERENDS-VAN ROON, J. M. (1950). Behaviour Suppl. 1, 1.")]

#zh(id: "R002")[#text("贝尔邦兹，G. P. & BAERENDS-VAN ROON, J. M. (1950)。行为补充。 1, 1.")]

#html.p(id: "en-R003")[#text("BREDER, G. M. (1959). Bull. Am. Mus. nat. Hist. 117, 395. BULLI& H. R., JR. (1960). Ecology 42, 194.")]

#zh(id: "R003")[#text("布雷德，通用汽车 (1959)。公牛。是。穆斯。自然。历史。 117, 395.布利&H.R.，JR。 （1960）。生态学 42, 194.")]

#html.p(id: "en-R004")[#text("CLARK, P. J. & EVANS, F. C. (1955).Science, N. K 121, 397.")]

#zh(id: "R004")[#text("克拉克，P.J. 和埃文斯，F.C. (1955)。《科学》，N.K 121, 397。")]

#html.p(id: "en-R005")[#text("CROOK, J. H. (1960). Behaviour 16, 1.")]

#zh(id: "R005")[#text("克鲁克，J.H.（1960）。行为 16, 1.")]

#html.p(id: "en-R006")[#text("DARLING, F. F. (1937). A Herdof Red Deer. Oxford: Oxford University Press.")]

#zh(id: "R006")[#text("亲爱的，F.F.（1937）。赫多夫红鹿。牛津：牛津大学出版社。")]

#html.p(id: "en-R007")[#text("E~PMARK, Y. (1968). Zoo/. Beitr. 14, 155.")]

#zh(id: "R007")[#text("E~PMARK, Y. (1968)。动物园/。拜特。 14、155。")]

#html.p(id: "en-R008")[#text("EVANS, U. R. (1945). Trans. Faraday Sot. 41,365.")]

#zh(id: "R008")[#text("埃文斯，U.R.（1945）。跨。法拉第索特。 41,365。")]

#html.p(id: "en-R009")[#text("FISHER, J. (1953). In Evolution us a Process. (J. Huxley et al., eds.), pp. 71-82. London: Allen and Unwin.")]

#zh(id: "R009")[#text("费舍尔，J.（1953）。在进化中我们是一个过程。 （J. Huxley 等人编辑），第 71-82 页。伦敦：艾伦和昂温。")]

#html.p(id: "en-R010")[#text("GALTON, F. (1871). Macmilkw’s Mag., Land. 23,353. F. (1883). Inquiries into Human Faculty and its Development. London: Dent; GALTON, (1928) New York: Dutton.")]

#zh(id: "R010")[#text("GALTON, F. (1871).麦克米尔克杂志，土地。 23,353. F. (1883).对人类教师及其发展的探究。 London: Dent;高尔顿，（1928）纽约：达顿。")]

#html.p(id: "en-R011")[#text("GILZIBRT, E. N. (1%2). Ann. math. Statist. 33, 958.")]

#zh(id: "R011")[#text("吉尔兹布特，E.N. (1%2)。安.数学。国家主义者。 33、958。")]

#html.p(id: "en-R012")[#text("HAMUTGN, W. D. (1963). Am. Nat. 97, 354.")]

#zh(id: "R012")[#text("HAMUTGN，W.D. (1963)。是。纳特。 97、354。")]

#html.p(id: "en-R013")[#text("HAMILTON, W. D. (1971). Proc. 3rd int. Symp. Smithson Instn (in the press).")]

#zh(id: "R013")[#text("汉密尔顿，W.D.（1971）。过程。第三名。症状。史密森研究所（新闻界）。")]

#html.p(id: "en-R014")[#text("HESSE, R., ALLEE, W. C. & SCHMIDT, K. P. (1937). Ecological Animal Geography. New York and London: Chapman, Wiley and Hall.")]

#zh(id: "R014")[#text("HESSE, R.、ALLEE, W. C. 和 SCHMIDT, K. P. (1937)。生态动物地理学。纽约和伦敦：查普曼、威利和霍尔。")]

#html.p(id: "en-R015")[#text("HOR~TMANN, E. (1952). Zoo/. Anz. Suppl. 17, 153.")]

#zh(id: "R015")[#text("霍~特曼，E. (1952)。动物园/。安兹。补编。 17、153。")]

#html.p(id: "en-R016")[#text("HUDLESTON, J. A. (1958). Entomologist’s mon. Mug. 94, 210.")]

#zh(id: "R016")[#text("哈德斯顿，J.A. (1958)。昆虫学家星期一。马克杯。 94、210。")]

#html.p(id: "en-R017")[#text("HUNTER, R. F. (1964). Advmt. Sci., Land. 21 (90) 29.")]

#zh(id: "R017")[#text("亨特，R.F. (1964)。 Advmt。科学，土地。 21（90）29。")]

#html.p(id: "en-R018")[#text("KRUUK, H. (1964). Behaviour Suppl. 11, 1.")]

#zh(id: "R018")[#text("克鲁克，H.（1964）。行为补充。 11, 1.")]

#html.p(id: "en-R019")[#text("LACK, D. (1968). Ecological Adaptations for Breeding in Birds. London: Methuen.")]

#zh(id: "R019")[#text("拉克，D.（1968）。鸟类繁殖的生态适应。伦敦：梅休因。")]

#html.p(id: "en-R020")[#text("LORENZ, K. (1966). On Aggression. London: Methuen.")]

#zh(id: "R020")[#text("洛伦茨，K. (1966)。关于侵略。伦敦：梅休因。")]

#html.p(id: "en-R021")[#text("MOORE, W. G. (1948). Turtox News 26,262.")]

#zh(id: "R021")[#text("摩尔，W.G. (1948)。海龟新闻 26,262。")]

#html.p(id: "en-R022")[#text("PRYER, H. (1884). Proc. zool. Sot. Land. 1884, 532. Scorn, J. P. (1945). Comp. Psychol. Monagr. 18 (96), l-29.")]

#zh(id: "R022")[#text("普赖尔，H. (1884)。过程。动物园。索特。土地。 1884, 532。斯考恩，J.P. (1945)。比较。心理。莫纳格拉。 18 (96)，l-29。")]

#html.p(id: "en-R023")[#text("SDOBNIKOV, V. M. (1935). Trudy arkt. nauchno-issled Inst. 24, 353.")]

#zh(id: "R023")[#text("斯多布尼科夫，V.M. (1935)。特鲁迪方舟。纳乌赫诺伊斯莱德研究所24、353。")]

#html.p(id: "en-R024")[#text("SPRINGER, S. (1957). Ecology 38,166.")]

#zh(id: "R024")[#text("斯普林格，S.（1957）。生态学38,166。")]

#html.p(id: "en-R025")[#text("TINBERGEN, N. (1951). The Study oflnstinct. Oxford: Oxford University Press.")]

#zh(id: "R025")[#text("廷伯根，N. (1951)。本能的研究。牛津：牛津大学出版社。")]

#html.p(id: "en-R026")[#text("TINBERGEN, N. (1953a). Social Behaviour in Animals. London: Methuen.")]

#zh(id: "R026")[#text("丁伯根，N.（1953a）。动物的社会行为。伦敦：梅休因。")]

#html.p(id: "en-R027")[#text("TINBERGEN, N. (19536). The Herring Gulf’s World. London: Collins.")]

#zh(id: "R027")[#text("廷伯根，N.（19536）。鲱鱼湾的世界。伦敦：柯林斯。")]

#html.p(id: "en-R028")[#text("WICKLER, W. (1968). Mimicry in Plants and Animals. London: Weidenfeld & Nicolson.")]

#zh(id: "R028")[#text("威克勒，W. (1968)。植物和动物的模仿。伦敦：魏登菲尔德和尼科尔森。")]

#html.p(id: "en-R029")[#text("WILLIAMS, G. C. (1964). Mich. St. Univ. Mus. Publ. Biol. Sev. 2, 351.")]

#zh(id: "R029")[#text("威廉姆斯，GC (1964)。密歇根圣大学穆斯。出版。生物。西弗。 2、351。")]

#html.p(id: "en-R030")[#text("WILLIAMS, G. C. (1966). Adaptation and Natural Selection. Princeton: Princeton University PUSS. WYNNB-EDWARDS, V. C. (1962). Animal Dispersion in Relation to Social Behaviour. Edinburgh: Oliver & Boyd.")]

#zh(id: "R030")[#text("威廉姆斯，GC (1966)。适应和自然选择。普林斯顿：普林斯顿大学 PUSS。 WYNNB-爱德华兹，V.C. (1962)。动物分散与社会行为的关系。爱丁堡：奥利弗和博伊德。")]

== Notes / 笔记

#html.p(id: "en-N001")[#text("Tinbergen (1953&l. Insects have another kind of “wolf in sheep’s clothing”: the predator mimicking its prey (Wickler, 1968).")]

#zh(id: "N001")[#text("Tinbergen（1953&l。昆虫有另一种“披着羊皮的狼”：捕食者模仿猎物（Wickler，1968）。")]
