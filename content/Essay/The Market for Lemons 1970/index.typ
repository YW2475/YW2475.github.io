#import "../index.typ": template, tufted
#import "../../_essay/bilingual.typ": zh
#show: template.with(
  title: "The Market for “Lemons”: Quality Uncertainty and the Market Mechanism",
  author: "George A. Akerlof",
  date: "1970",
  description: "买家难以分辨质量时，好商品为什么可能退出市场？",
  lang: "en",
  css: ("/assets/custom.css", "/assets/essay.css"),
)

= The Market for “Lemons”: Quality Uncertainty and the Market Mechanism / “柠檬”市场：质量不确定性与市场机制

== I. Introduction / I. 引言

#html.p(id: "en-S001")[#text("This paper relates quality and uncertainty. The existence of goods of many grades poses interesting and important problems for the theory of markets. On the one hand, the interaction of quality differences and uncertainty may explain important institutions of the labor market. On the other hand, this paper presents a struggling attempt to give structure to the statement: \"Business in underdeveloped countries is difficult\"; in particular, a structure is given for determining the economic costs of dishonesty. Additional applications of the theory include comments on the structure of money markets, on the notion of \"insurability,\" on the liquidity of durables, and on brand-name goods.")]

#zh(id: "S001")[#text("本文涉及质量和不确定性。多种等级商品的存在给市场理论提出了有趣且重要的问题。一方面，质量差异和不确定性的相互作用可以解释劳动力市场的重要制度。另一方面，本文提出了一种努力的尝试，试图为“不发达国家的生意很困难”这一说法提供结构；特别是，给出了确定不诚实的经济成本的结构。该理论的其他应用包括对货币市场结构、“可保性”概念、耐用品流动性和品牌商品的评论。")]

#html.p(id: "en-S002")[#text("There are many markets in which buyers use some market statistic to judge the quality of prospective purchases. In this case there is incentive for sellers to market poor quality merchandise, since the returns for good quality accrue mainly to the entire group whose statistic is affected rather than to the individual seller. As a result there tends to be a reduction in the average quality of goods and also in the size of the market. It should also be perceived that in these markets social and private returns differ, and therefore, in some cases, governmental intervention may increase the welfare of all parties. Or private institutions may arise to take advantage of the potential increases in welfare which can accrue to all parties. By nature, however, these institutions are nonatomistic, and therefore concentrations of power - with ill consequences of their own can develop.")]

#zh(id: "S002")[#text("在许多市场中，买家使用一些市场统计数据来判断预期购买的质量。在这种情况下，卖家就有动力销售劣质商品，因为优质商品的回报主要归于统计数据受影响的整个群体，而不是个人卖家。结果，商品的平均质量和市场规模往往会下降。还应该认识到，在这些市场中，社会和私人回报是不同的，因此，在某些情况下，政府干预可能会增加各方的福利。或者，私人机构可能会出现，利用各方可能获得的潜在福利增加。然而，从本质上讲，这些机构是非原子性的，因此权力的集中可能会发展，从而带来不良后果。")]

#html.p(id: "en-S003")[#text("The automobile market is used as a finger exercise to illustrate and develop these thoughts. It should be emphasized that this market is chosen for its concreteness and ease in understanding rather than for its importance or realism.")]

#zh(id: "S003")[#text("汽车市场被用作一个手指练习来说明和发展这些想法。应该强调的是，选择这个市场是因为它的具体性和易于理解，而不是因为它的重要性或现实性。")]

== II. THE MODEL WITH AUTOMOBILES AS AN EXAMPLE / 二.以汽车为例的模型

== A. The Automobiles Market / A. 汽车市场

#html.p(id: "en-S004")[#text("The example of used cars captures the essence of the problem. From time to time one hears either mention of or surprise at the large price difference between new cars and those which have just left the showroom. The usual lunch table justification for this phenomenon is the pure joy of owning a \"new\" car. We offer a different explanation. Suppose (for the sake of clarity rather than reality) that there are just four kinds of cars. There are new cars and used cars. There are good cars and bad cars (which in America are known as \"lemons\"). A new car may be a good car or a lemon, and of course the same is true of used cars.")]

#zh(id: "S004")[#text("二手车的例子抓住了问题的本质。有时，人们会听到有人提到或惊讶于新车与刚刚离开展厅的车之间的巨大价格差异。通常午餐桌上对这种现象的解释是拥有一辆“新车”的纯粹快乐。我们提供不同的解释。假设（为了清楚起见而不是为了现实）只有四种汽车。有新车和二手车。有好车和坏车（在美国被称为“柠檬”）。新车可能是好车，也可能是次品，当然二手车也是如此。")]

#html.p(id: "en-S005")[#text("The individuals in this market buy a new automobile without knowing whether the car they buy will be good or a lemon. But they do know that with probability q it is a good car and with probability (1-q) it is a lemon; by assumption, q is the proportion of good cars produced and (1 - q) is the proportion of lemons.")]

#zh(id: "S005")[#text("这个市场上的个人购买新车时并不知道他们购买的汽车是好车还是次品。但他们确实知道，以 q 的概率，它是一辆好车，以 (1-q) 的概率，它是一辆柠檬车；假设，q 是生产的好车的比例，(1 - q) 是柠檬的比例。")]

#html.p(id: "en-S006")[#text("After owning a specific car, however, for a length of time, the car owner can form a good idea of the quality of this machine; i.e., the owner assigns a new probability to the event that his car is a lemon. This estimate is more accurate than the original estimate. An asymmetry in available information has developed: for the sellers now have more knowledge about the quality of a car than the buyers. But good cars and bad cars must still sell at the same price -since it is impossible for a buyer to tell the difference between a good car and a bad car. It is apparent that a used car cannot have the same valuation as a new car - if it did have the same valuation, it would clearly be advantageous to trade a lemon at the price of new car, and buy another new car, at a higher probability q of being good and a lower probability of being bad. Thus the owner of a good machine must be locked in. Not only is it true that he cannot receive the true value of his car, but he cannot even obtain the expected value of a new car.")]

#zh(id: "S006")[#text("然而，当拥有一辆特定的汽车一段时间后，车主就会对这台机器的质量形成一个很好的认识；也就是说，车主为他的车是柠檬车的事件分配了一个新的概率。这个估计比原来的估计更准确。可用信息的不对称已经出现：因为现在卖家比买家更了解汽车的质量。但好车和坏车仍然必须以相同的价格出售——因为买家不可能区分好车和坏车。显然，二手车不可能具有与新车相同的估值 - 如果它确实具有相同的估值，那么以新车的价格交易柠檬并购买另一辆新车显然是有利的，好车的概率 q 较高，坏车的概率 q 较低。因此，一台好机器的拥有者必须被锁定。他不仅无法获得汽车的真实价值，甚至无法获得新车的预期价值。")]

#html.p(id: "en-S007")[#text("Gresham's law has made a modified reappearance. For most cars traded will be the \"lemons,\" and good cars may not be traded at all. The \"bad\" cars tend to drive out the good (in much the same way that bad money drives out the good). But the analogy with Gresham's law is not quite complete: bad cars drive out the good because they sell at the same price as good cars; similarly, bad money drives out good because the exchange rate is even. But the bad cars sell at the same price as good cars since it is impossible for a buyer to tell the difference between a good and a bad car; only the seller knows. In Gresham's law, however, presumably both buyer and seller can tell the difference between good and bad money. So the analogy is instructive, but not complete.")]

#zh(id: "S007")[#text("格雷欣定律经过修改再现。对于大多数交易的汽车来说，都是“柠檬”，而好车可能根本无法交易。 “劣质”汽车往往会赶走好车（就像劣币驱逐良币一样）。但与格雷欣定律的类比并不完全：劣质车驱逐良品，因为它们的售价与好车相同；同样，劣币驱逐良币，因为汇率是均匀的。但劣质车与好车的售价相同，因为买家无法区分好车和劣质车；只有卖家知道。然而，根据格雷欣法则，买家和卖家想必都能辨别好钱和劣币。所以这个类比是有启发性的，但并不完整。")]

== B. Asymmetrical Information / B. 信息不对称

#html.p(id: "en-S008")[#text("It has been seen that the good cars may be driven out of the market by the lemons. But in a more continuous case with different grades of goods, even worse pathologies can exist. For it is quite possible to have the bad driving out the not-so-bad driving out the medium driving out the not-so-good driving out the good in such a sequence of events that no market exists at all.")]

#zh(id: "S008")[#text("可见，好车可能会被柠檬赶出市场。但在不同等级商品的更连续的情况下，可能存在更严重的病症。因为在这样的一系列事件中，很可能会出现坏的驱逐不太坏的驱逐中等的驱逐不太好的驱逐好的，以至于根本不存在市场。")]

#html.p(id: "en-S009")[#text("One can assume that the demand for used automobiles depends most strongly upon two variables—the price of the automobile p and the average quality of used cars traded, μ, or Qᵈ = D(p, μ). Both the supply of used cars and also the average quality μ will depend upon the price, or μ = μ(p) and S = S(p). And in equilibrium the supply must equal the demand for the given average quality, or S(p) = D(p, μ(p)). As the price falls, normally the quality will also fall. And it is quite possible that no goods will be traded at any price level.")]

#zh(id: "S009")[#text("我们可以假设对二手车的需求很大程度上取决于两个变量——汽车的价格 p 和二手车交易的平均质量 μ，或 Qᵈ = D(p, μ)。二手车的供应量和平均质量 μ 都取决于价格，即 μ = μ(p) 且 S = S(p)。在均衡状态下，供给必须等于给定平均质量的需求，即 S(p) = D(p, μ(p))。随着价格下降，通常质量也会下降。而且很有可能没有任何商品能够以任何价格水平进行交易。")]

#html.p(id: "en-S010")[#text("Such an example can be derived from utility theory. Assume that there are just two groups of traders: groups one and two. Give group one a utility function")]

#zh(id: "S010")[#text("这样的例子可以从效用理论中推导出来。假设只有两组交易者：第一组和第二组。给第一组一个效用函数")]

#html.figure(id: "E001", class: "essay-equation")[
  #image("assets/equation-01.png")
]

#html.p(id: "en-S011")[#text("where M is the consumption of goods other than automobiles, x is the quality of the ith automobile,and n is the number of automobiles. Similarly, let")]

#zh(id: "S011")[#text("其中M是汽车以外的商品消费，x是第i辆汽车的质量，n是汽车的数量。同样，让")]

#html.figure(id: "E002", class: "essay-equation")[
  #image("assets/equation-02.png")
]

#html.p(id: "en-S012")[#text("where M, xi, and n are defined as before.")]

#zh(id: "S012")[#text("其中 M、xi 和 n 的定义如前。")]

#html.p(id: "en-S013")[#text("Three comments should be made about these utility functions: (1) without linear utility (say with logarithmic utility) one gets needlessly mired in algebraic complication. (2) The use of linear utility allows a focus on the effects of asymmetry of information; with a concave utility function we would have to deal jointly with the usual risk-variance effects of uncertainty and the special effects we wish to discuss here. (3) U₁ and U₂ have the odd characteristic that the addition of a second car, or indeed a kth car, adds the same amount of utility as the first. Again realism is sacrificed to avoid a diversion from the proper focus.")]

#zh(id: "S013")[#text("关于这些效用函数，应该做三点评论：（1）如果没有线性效用（比如对数效用），人们就会不必要地陷入代数复杂性的泥潭。 （2）线性效用的使用可以关注信息不对称的影响；对于凹效用函数，我们必须共同处理不确定性的常见风险方差效应以及我们希望在这里讨论的特殊效应。 (3) U₁ 和 U2 有一个奇怪的特性，即添加第二辆车，或者实际上是第 k 辆车，增加了与第一辆车相同数量的效用。再次牺牲现实主义以避免偏离正确的焦点。")]

#html.p(id: "en-S014")[#text("To continue, it is assumed (1) that both type one traders and type two traders are von Neumann-Morgenstern maximizers of expected utility; (2) that group one has N cars with uniformly distributed quality x, 0 ≤ x ≤ 2, and group two has no cars; (3) that the price of \"other goods\" M is unity.")]

#zh(id: "S014")[#text("继续，假设 (1) 第一类交易者和第二类交易者都是预期效用的冯·诺依曼-摩根斯坦最大化者； (2)第一组有N辆车，质量x均匀分布，0≤x≤2，第二组没有车； (3)“其他商品”M的价格是统一的。")]

#html.p(id: "en-S015")[#text("Denote the income (including that derived from the sale of automobiles) of all type one traders as Y1 and the income of all type two traders as Y2. The demand for used cars will be the sum of the demands by both groups. When one ignores indivisibilities, the demand for automobiles by type one traders will be")]

#zh(id: "S015")[#text("将所有第一类贸易商的收入（包括汽车销售收入）记为Y1，将所有第二类贸易商的收入记为Y2。对二手车的需求将是两个群体需求的总和。当人们忽略不可分割性时，第一类贸易商对汽车的需求将是")]

#html.figure(id: "E003", class: "essay-equation")[
  #image("assets/equation-03.png")
]

#html.p(id: "en-S016")[#text("And the supply of cars offered by type one traders is")]

#zh(id: "S016")[#text("第一类贸易商提供的汽车供应量为")]

#html.figure(id: "E004", class: "essay-equation")[
  #image("assets/equation-04.png")
]

#html.p(id: "en-S017")[#text("with average quality")]

#zh(id: "S017")[#text("质量一般")]

#html.figure(id: "E005", class: "essay-equation")[
  #image("assets/equation-05.png")
]

#html.p(id: "en-S018")[#text("(To derive (1) and (2), the uniform distribution of automobile quality is used.)")]

#zh(id: "S018")[#text("（推导（1）和（2）时，使用了汽车质量的均匀分布。）")]

#html.p(id: "en-S019")[#text("Similarly the demand of type two traders is")]

#zh(id: "S019")[#text("同样，第二类交易者的需求是")]

#html.figure(id: "E006", class: "essay-equation")[
  #image("assets/equation-06.png")
]

#html.p(id: "en-S020")[#text("and")]

#zh(id: "S020")[#text("和")]

#html.figure(id: "E007", class: "essay-equation")[
  #image("assets/equation-07.png")
]

#html.p(id: "en-S021")[#text("Thus total demand D (p, u) is")]

#zh(id: "S021")[#text("因此总需求 D (p, u) 为")]

#html.figure(id: "E008", class: "essay-equation")[
  #image("assets/equation-08.png")
]

#html.p(id: "en-S022")[#text("However, with price p, average quality is p/2 and therefore at no price will any trade take place at all: in spite of the fact that at any given price between 0 and 3 there are traders of type one who are willing to sell their automobiles at a price which traders of type two are willing to pay.")]

#zh(id: "S022")[#text("然而，在价格为 p 的情况下，平均质量为 p/2，因此在任何价格下都不会发生任何交易：尽管事实是，在 0 到 3 之间的任何给定价格下，第一类交易者愿意以第二类交易者愿意支付的价格出售他们的汽车。")]

== C. Symmetric Information / C. 对称信息

#html.p(id: "en-S023")[#text("The foregoing is contrasted with the case of symmetric information. Suppose that the quality of all cars is uniformly distributed, O<x-2. Then the demand curves and supply curves can be written as follows: Supply")]

#zh(id: "S023")[#text("上述情况与对称信息的情况形成对比。假设所有汽车的质量均匀分布，O<x-2。那么需求曲线和供给曲线可以写成如下： 供给")]

#html.figure(id: "E009", class: "essay-equation")[
  #image("assets/equation-09.png")
]

#html.p(id: "en-S024")[#text("And the demand curves are")]

#zh(id: "S024")[#text("需求曲线是")]

#html.figure(id: "E010", class: "essay-equation")[
  #image("assets/equation-10.png")
]

#html.p(id: "en-S025")[#text("In equilibrium")]

#zh(id: "S025")[#text("处于平衡状态")]

#html.figure(id: "E011", class: "essay-equation")[
  #image("assets/equation-11.png")
]

#html.p(id: "en-S026")[#text("If N<Y2 there is a gain in utility over the case of asymmetrical information of N/2. (If N> Y2, in which case the income of type two traders is insufficient to buy all N automobiles, there is a gain in utility of Y2/2 units.)")]

#zh(id: "S026")[#text("如果 N<Y2，则与 N/2 的不对称信息的情况相比，效用有所增加。 （如果 N > Y2，在这种情况下，第二类交易者的收入不足以购买所有 N 辆汽车，则 Y2/2 单位的效用会增加。）")]

#html.p(id: "en-S027")[#text("Finally, it should be mentioned that in this example, if traders of groups one and two have the same probabilistic estimates about the quality of individual automobiles - though these estimates may vary from automobile to automobile - (3), (4), and (5) will still describe equilibrium with one slight change: p will then represent the expected price of one quality unit.")]

#zh(id: "S027")[#text("最后，应该提到的是，在这个例子中，如果第一组和第二组的交易者对单辆汽车的质量有相同的概率估计——尽管这些估计可能因汽车而异——（3）、（4）和（5）仍然会描述有一个微小变化的均衡：p将代表一个质​​量单位的预期价格。")]

== III. EXAMPLES AND APPLICATIONS / 三．示例和应用

== A. Insurance / A、保险

#html.p(id: "en-S028")[#text("It is a well-known fact that people over 65 have great difficulty in buying medical insurance. The natural question arises: why doesn't the price rise to match the risk?")]

#zh(id: "S028")[#text("众所周知，65岁以上的老年人购买医疗保险非常困难。自然的问题出现了：为什么价格没有上涨以匹配风险？")]

#html.p(id: "en-S029")[#text("Our answer is that as the price level rises the people who insure themselves will be those who are increasingly certain that they will need the insurance; for error in medical check-ups, doctors' sympathy with older patients, and so on make it much easier for the applicant to assess the risks involved than the insurance company. The result is that the average medical condition of insurance applicants deteriorates as the price level rises -with the result that no insurance sales may take place at any price.' This is strictly analogous to our automobiles case, where the average quality of used cars supplied fell with a corresponding fall in the price level. This agrees with the explanation in insurance textbooks:")]

#zh(id: "S029")[#text("我们的答案是，随着物价水平的上升，为自己投保的人将是那些越来越确定自己需要保险的人；由于体检失误、医生对老年患者的同情心等，使得投保人比保险公司更容易评估所涉及的风险。其结果是，投保人的平均医疗状况随着物价水平的上升而恶化，导致任何价格都无法进行保险销售。这与我们的汽车案例严格类似，二手车供应的平均质量随着价格水平的下降而下降。这与保险教科书中的解释一致：")]

#html.p(id: "en-S030")[#text("Generally speaking policies are not available at ages materially greater than sixty-five.... The term premiums are too high for any but the most pessimistic (which is to say the least healthy) insureds to find attractive. Thus there is a severe problem of adverse selection at these ages.2")]

#zh(id: "S030")[#text("一般来说，保单不适用于实质上超过六十五岁的人……定期保费对于除了最悲观（也就是说最不健康）的被保险人之外的任何人都有吸引力。因此，这些年龄段存在严重的逆向选择问题2。")]

#html.p(id: "en-S031")[#text("The statistics do not contradict this conclusion. While demands for health insurance rise with age, a 1956 national sample survey of 2,809 families with 8,898 persons shows that hospital insurance coverage drops from 63 per cent of those aged 45 to 54, to 31 per cent for those over 65. And surprisingly, this survey also finds average medical expenses for males aged 55 to 64 of $88, while males over 65 pay an average of $77.3 While noninsured expenditure rises from $66 to $80 in these age groups, insured expenditure declines from $105 to $70. The conclusion is tempting that insurance companies are particularly wary of giving medical insurance to older people.")]

#zh(id: "S031")[#text("统计数据与这一结论并不矛盾。虽然健康保险的需求随着年龄的增长而增加，但 1956 年对 2,809 个家庭、8,898 人进行的全国抽样调查显示，医院保险覆盖率从 45 岁至 54 岁的 63% 下降到 65 岁以上的 31%。令人惊讶的是，这项调查还发现，55 岁至 64 岁的男性平均医疗费用为 88 美元，而 65 岁以上的男性平均支付 77.3 美元，而无保险支出这些年龄段的保险支出从 66 美元上升到 80 美元，保险支出从 105 美元下降到 70 美元。结论很诱人，保险公司对于向老年人提供医疗保险尤其谨慎。")]

#html.p(id: "en-S032")[#text("The principle of \"adverse selection\" is potentially present in all lines of insurance. The following statement appears in an insurance textbook written at the Wharton School:")]

#zh(id: "S032")[#text("“逆向选择”原则可能存在于所有保险领域。以下陈述出现在沃顿商学院编写的一本保险教科书中：")]

#html.p(id: "en-S033")[#text("There is potential adverse selection in the fact that healthy term insurance policy holders may decide to terminate their coverage when they become older and premiums mount. This action could leave an insurer with an undue proportion of below average risks and claims might be higher than anticipated. Adverse selection \"appears (or at least is possible) whenever the individual or group insured has freedom to buy or not to buy, to choose the amount or plan of insurance, and to persist or to discontinue as a policy holder.\" '")]

#zh(id: "S033")[#text("事实上，健康定期保险保单持有人可能会在年龄增长且保费增加时决定终止保险，从而存在潜在的逆向选择。这一行动可能会给保险公司带来不适当比例的低于平均水平的风险，并且索赔可能高于预期。逆向选择“只要个人或团体被保险人有购买或不购买的自由、选择保险金额或保险计划、以及继续或终止作为保单持有人的自由，就会出现（或至少是可能的）。” '")]

#html.p(id: "en-S034")[#text("Group insurance, which is the most common form of medical insurance in the United States, picks out the healthy, for generally")]

#zh(id: "S034")[#text("团体保险是美国最常见的医疗保险形式，选择健康的人，一般情况下")]

#html.p(id: "en-S035")[#text("1. Arrow's fine article, \"Uncertainty and Medical Care\" (American Economic Review, Vol. 53, 1963), does not make this point explicitly. He emadequate health is a precondition for employment. At the same time this means that medical insurance is least available to those who need it most, for the insurance companies do their own \"adverse selection.\"")]

#zh(id: "S035")[#text("1. 阿罗的好文《不确定性与医疗保健》（《美国经济评论》，第 53 卷，1963 年）并没有明确指出这一点。他把健康作为就业的先决条件。同时，这也意味着医疗保险对于最需要的人来说是最难获得的，因为保险公司会进行自己的“逆向选择”。")]

#html.p(id: "en-S036")[#text("This adds one major argument in favor of medicare.5 On a cost benefit basis medicare may pay off: for it is quite possible that every individual in the market would be willing to pay the expected cost of his medicare and buy insurance, yet no insurance company can afford to sell him a policy - for at any price it will attract too many \"lemons.\" The welfare economics of medicare, in this view, is exactly analogous to the usual classroom argument for public expenditure on roads.")]

#zh(id: "S036")[#text("这增加了支持医疗保险的一个主要论据。5 在成本效益的基础上，医疗保险可能会得到回报：因为很可能市场上的每个人都愿意支付其医疗保险的预期成本并购买保险，但没有一家保险公司有能力向他出售保单 - 因为无论价格如何，它都会吸引太多的“柠檬”。在这种观点下，医疗保险的福利经济学与课堂上有关道路公共支出的常见争论完全相似。")]

== B. The Employment of Minorities / B. 少数族裔的就业

#html.p(id: "en-S037")[#text("The Lemons Principle also casts light on the employment of minorities. Employers may refuse to hire members of minority groups for certain types of jobs. This decision may not reflect irrationality or prejudice -but profit maximization. For race may serve as a good statistic for the applicant's social background, quality of schooling, and general job capabilities.")]

#zh(id: "S037")[#text("柠檬原则也阐明了少数族裔的就业问题。雇主可能会拒绝雇用少数群体成员从事某些类型的工作。这一决定可能并不反映非理性或偏见，而是反映利润最大化。因为种族可以作为申请人社会背景、教育质量和一般工作能力的良好统计数据。")]

#html.p(id: "en-S038")[#text("Good quality schooling could serve as a substitute for this statistic; by grading students the schooling system can give a better indicator of quality than other more superficial characteristics. As T. W. Schultz writes, \"The educational establishment discovers and cultivates potential talent. The capabilities of children and mature students can never be known until found and cultivated.\" 6 (Italics added.) An untrained worker may have valuable natural talents, but these talents must be certified by \"the educational establishment\" before a company can afford to use them. The certifying establishment, however, must be credible; the unreliability of slum schools decreases the economic possibilities of their students. This lack may be particularly disadvantageous to members of already disadvantaged minority groups. For an employer may make a rational decision not to hire any members of these groups in responsible positions - because it is difficult to distinguish those with good job qualifications from those with bad qualifications. This type of decision is clearly what George Stigler had in mind when he wrote, \"in a regime of ignorance Enrico Fermi would have been a gardener, Von Neumann a checkout clerk at a drugstore.\" 7")]

#zh(id: "S038")[#text("高质量的学校教育可以替代这一统计数据；通过对学生进行评分，学校教育系统可以比其他更肤浅的特征提供更好的质量指标。正如 T. W. 舒尔茨 (T. W. Schultz) 所写，“教育机构发现并培养潜在人才。儿童和成熟学生的能力只有在被发现和培养后才能被认识。” 6（斜体字已添加。）未经培训的工人可能拥有宝贵的天赋，但这些天赋必须经过“教育机构”的认证，公司才有能力使用它们。然而，认证机构必须是可信的；贫民窟学校的不可靠性降低了学生的经济可能性。这种缺乏可能对已经处于不利地位的少数群体的成员尤其不利。因为雇主可能会做出理性的决定，不雇用这些群体中的任何成员担任负责的职位——因为很难区分那些具有良好工作资格的人和那些具有不良资格的人。这种类型的决定显然正是乔治·斯蒂格勒在他写道时所想到的，“在无知的政权下，恩里科·费米可能是一名园丁，冯·诺依曼可能是一家药店的收银员。” 7")]

#html.p(id: "en-S039")[#text("As a result, however, the rewards for work in slum schools tend to accrue to the group as a whole -in raising its average quality -rather than to the individual. Only insofar as information in addition to race is used is there any incentive for training.")]

#zh(id: "S039")[#text("然而，其结果是，贫民窟学校的工作回报往往归于整个群体——提高其平均质量——而不是个人。只有使用除种族之外的信息，才有训练的动力。")]

#html.p(id: "en-S040")[#text("An additional worry is that the Office of Economic Opportunity is going to use cost-benefit analysis to evaluate its programs. For many benefits may be external. The benefit from training minority groups may arise as much from raising the average quality of the group as from raising the quality of the individual trainee; and, likewise, the returns may be distributed over the whole group rather than to the individual.")]

#zh(id: "S040")[#text("另一个担忧是经济机会办公室将使用成本效益分析来评估其计划。因为许多好处可能是外部的。培训少数群体的好处可能来自于提高该群体的平均素质，也可能来自于提高个别受训者的素质；同样，回报可以分配给整个群体而不是个人。")]

== C. The Costs of Dishonesty / C. 不诚实的代价

#html.p(id: "en-S041")[#text("The Lemons model can be used to make some comments on the costs of dishonesty. Consider a market in which goods are sold honestly or dishonestly; quality may be represented, or it may be misrepresented. The purchaser's problem, of course, is to identify quality. The presence of people in the market who are willing to offer inferior goods tends to drive the market out of existence - as in the case of our automobile \"lemons.\" It is this possibility that represents the major costs of dishonesty - for dishonest dealings tend to drive honest dealings out of the market. There may be potential buyers of good quality products and there may be potential sellers of such products in the appropriate price range; however, the presence of people who wish to pawn bad wares as good wares tends to drive out the legitimate business. The cost of dishonesty, therefore, lies not only in the amount by which the purchaser is cheated; the cost also must include the loss incurred from driving legitimate business out of existence.")]

#zh(id: "S041")[#text("柠檬模型可以用来对不诚实的成本做出一些评论。考虑一个诚实或不诚实销售商品的市场；质量可能会得到体现，也可能会被歪曲。购买者的问题当然是鉴定质量。市场上那些愿意提供劣质商品的人往往会导致市场不复存在——就像我们的汽车“柠檬”的情况一样。正是这种可能性代表了不诚实的主要成本——因为不诚实的交易往往会将诚实的交易逐出市场。可能存在优质产品的潜在买家，也可能存在适当价格范围内此类产品的潜在卖家；然而，那些想把劣质商品当成好商品的人的存在往往会驱逐合法的生意。因此，不诚实的成本不仅在于购买者被欺骗的金额，还在于购买者被欺骗的金额。成本还必须包括因合法业务不复存在而造成的损失。")]

#html.p(id: "en-S042")[#text("Dishonesty in business is a serious problem in underdeveloped countries. Our model gives a possible structure to this statement and delineates the nature of the \"external\" economies involved. In particular, in the model economy described, dishonesty, or the")]

#zh(id: "S042")[#text("商业不诚实是欠发达国家的一个严重问题。我们的模型为这一陈述提供了一个可能的结构，并描述了所涉及的“外部”经济的性质。特别是，在所描述的模型经济中，不诚实或")]

#html.p(id: "en-S043")[#text("7. G. J. Stigler, \"Information and the Labor Market,\" Journal of Politiutility per automobile; furthermore, it reduces the size of the used car market from N to 0. We can, consequently, directly evaluate the costs of dishonesty - at least in theory.")]

#zh(id: "S043")[#text("7. G. J. Stigler，“信息与劳动力市场”，《每辆汽车的政治效用杂志》；此外，它将二手车市场的规模从 N 减少到 0。因此，我们可以直接评估不诚实的成本——至少在理论上是这样。")]

#html.p(id: "en-S044")[#text("There is considerable evidence that quality variation is greater in underdeveloped than in developed areas. For instance, the need for quality control of exports and State Trading Corporations can be taken as one indicator. In India, for example, under the Export Quality Control and Inspection Act of 1963, \"about 85 per cent of Indian exports are covered under one or the other type of quality control.\" 8 Indian housewives must carefully glean the rice of the local bazaar to sort out stones of the same color and shape which have been intentionally added to the rice. Any comparison of the heterogeneity of quality in the street market and the canned qualities of the American supermarket suggests that quality variation is a greater problem in the East than in the West.")]

#zh(id: "S044")[#text("有大量证据表明，欠发达地区的质量差异比发达地区更大。例如，出口和国营贸易公司的质量控制需求可以作为一项指标。例如，在印度，根据 1963 年《出口质量控制和检验法》，“大约 85% 的印度出口产品受到一种或另一种类型的质量控制”。 8 印度家庭主妇必须仔细拾取当地集市的大米，挑选出故意添加到大米中的颜色和形状相同的石头。对街头市场的质量异质性和美国超市的罐装质量的任何比较都表明，质量差异在东方是一个比西方更大的问题。")]

#html.p(id: "en-S045")[#text("In one traditional pattern of development the merchants of the pre-industrial generation turn into the first entrepreneurs of the next. The best-documented case is Japan,9 but this also may have been the pattern for Britain and America.' In our picture the important skill of the merchant is identifying the quality of merchandise; those who can identify used cars in our example and can guarantee the quality may profit by as much as the difference between type two traders' buying price and type one traders' selling price. These people are the merchants. In production these skills are equally necessary - both to be able to identify the quality of inputs and to certify the quality of outputs. And this is one (added) reason why the merchants may logically become the first entrepreneurs. The problem, of course, is that entrepreneurship may be a scarce resource; no development text leaves entrepreneurship unemphasized. Some treat it as central.2 Given, then, that entrepreneurship is scarce, there are two ways in which product variations impede development. First, the pay-off to trade is great for wouldbe entrepreneurs, and hence they are diverted from production; second, the amount of entrepreneurial time per unit output is greater, the greater are the quality variations.")]

#zh(id: "S045")[#text("在一种传统的发展模式中，前工业化一代的商人变成了下一代的第一批企业家。记录最齐全的案例是日本，9 但这也可能是英国和美国的模式。在我们的图中，商家的重要技能是识别商品的质量；在我们的例子中，那些能够识别二手车并且能够保证质量的人可以获得与第二类交易者的买入价和第一类交易者的卖出价之间的差额一样多的利润。这些人就是商人。在生产中，这些技能同样必要——既能够识别投入的质量，又能够证明产出的质量。这就是商人顺理成章地成为第一批企业家的一个（补充的）原因。当然，问题在于创业精神可能是一种稀缺资源；任何发展文本都不会忽视创业精神。有些人将其视为核心。2鉴于创业精神稀缺，产品差异有两种方式阻碍发展。首先，贸易的回报对于潜在的企业家来说是巨大的，因此他们从生产中转移；其次，单位产出的创业时间越多，质量差异越大。")]

== D. Credit Markets in Underdeveloped Countries / D. 不发达国家的信贷市场

#html.p(id: "en-S046")[#text("(1) Credit markets in underdeveloped countries often strongly reflect the operation of the Lemons Principle. In India a major fraction of industrial enterprise is controlled by managing agencies (according to a recent survey, these \"managing agencies\" controlled 65.7 per cent of the net worth of public limited companies and 66 per cent of total assets).3 Here is a historian's account of the function and genesis of the \"managing agency system\":")]

#zh(id: "S046")[#text("(1)不发达国家的信贷市场往往强烈地体现了柠檬原则的运作。在印度，大部分工业企业由管理机构控制（根据最近的一项调查，这些“管理机构”控制着公共有限公司净值的 65.7% 和总资产的 66%）。3 以下是一位历史学家对“管理机构制度”的功能和起源的描述：")]

#html.p(id: "en-S047")[#text("The management of the South Asian commercial scene remained the function of merchant houses, and a type of organization peculiar to South Asia known as the Managing Agency. When a new venture was promoted (such as a manufacturing plant, a plantation, or a trading venture), the promoters would approach an established managing agency. The promoters might be Indian or British, and they might have technical or financial resources or merely a concession. In any case they would turn to the agency because of its reputation, which would encourage confidence in the venture and stimulate investment.'")]

#zh(id: "S047")[#text("南亚商业场景的管理仍然是商人行的职能，以及南亚特有的一种组织类型，称为管理机构。当一个新的企业（例如制造厂、种植园或贸易企业）得到推广时，发起人会联系一个已建立的管理机构。发起人可能是印度人或英国人，他们可能拥有技术或财政资源，或者仅仅是让步。无论如何，他们都会因为该机构的声誉而求助于该机构，这将增强人们对企业的信心并刺激投资。")]

#html.p(id: "en-S048")[#text("In turn, a second major feature of the Indian industrial scene has been the dominance of these managing agencies by caste (or, more accurately, communal) groups. Thus firms can usually be classified according to communal origin.5 In this environment, in which outside investors are likely to be bilked of their holdings, either (1) firms establish a reputation for \"honest\" dealing, which confers upon them a monopoly rent insofar as their services are limited in supply, or (2) the sources of finance are communal groups which can use communal -and possibly familial - ties to encourage honest dealing within the community. It is, in Indian economic history, extraordinarily difficult to discern whether the savings of rich landlords failed to be invested in the industrial sector (1) because of a fear to invest in ventures controlled by other communities, (2) because of inflated propensities to consume, or (3) because of low rates of return.6 At the very least, however, it is clear that the British-owned managing agencies tended to have an equity holding whose communal origin was more heterogeneous than the Indian-controlled agency houses, and would usually include both Indian and British investors.")]

#zh(id: "S048")[#text("反过来，印度工业界的第二个主要特征是种姓（或更准确地说，社区）群体对这些管理机构的主导地位。因此，企业通常可以根据公共起源进行分类。 5 在这种环境下，外部投资者可能会被骗取其所持股份，要么（1）企业建立了“诚实”交易的声誉，这在其服务供应有限的情况下赋予它们垄断租金，要么（2）资金来源是公共团体，它们可以利用公共（可能还有家族）关系来鼓励社区内的诚实交易。在印度经济史上，很难辨别富裕地主的储蓄是否未能投资于工业部门（1）是因为害怕投资于其他社区控制的企业，（2）是因为消费倾向膨胀，还是（3）是因为回报率低。 6 然而，至少很明显，英国拥有的管理机构往往拥有其共同起源比印度控制的代理机构更加异质的股权，并且通常包括印度和英国投资者。")]

#html.figure(id: "T001", class: "essay-paper-figure")[
  #image("assets/table-12.png")
]

#zh(id: "T001")[#text("工业控制权按社群分布。年份：1911、1931、1951。各行：英国人、帕西人、古吉拉特人、犹太人、穆斯林、孟加拉人、马尔瓦里人、混合控制、合计。")]

#html.p(id: "en-S049")[#text("(2) A second example of the workings of the Lemons Principle concerns the extortionate rates which the local moneylender charges his clients. In India these high rates of interest have been the leading factor in landlessness; the so-called \"Cooperative Movement\" was meant to counteract this growing landlessness by setting up banks to compete with the local moneylenders.7 While the large banks in the central cities have prime interest rates of 6, 8, and 10 per cent, the local moneylender charges 15, 25, and even 50 per cent. The answer to this seeming paradox is that credit is granted only where the granter has (1) easy means of enforcing his contract or (2) personal knowledge of the character of the borrower. The middleman who tries to arbitrage between the rates of the moneylender and the central bank is apt to attract all the \"lemons\" and thereby make a loss.")]

#zh(id: "S049")[#text("(2) 柠檬原则运作的第二个例子涉及当地放债人向其客户收取的勒索利率。在印度，高利率是导致无土地的主要原因。所谓的“合作社运动”旨在通过设立银行与当地放债人竞争来应对日益严重的失地现象。7 虽然中心城市的大型银行的优惠利率为 6%、8% 和 10%，但当地放债人的收费为 15%、25% 甚至 50%。这个看似悖论的答案是，只有在授予者拥有（1）执行合同的简单手段或（2）个人了解借款人的性格时，才会授予信贷。试图在放债人和央行利率之间进行套利的中间人很容易吸引所有“柠檬”，从而蒙受损失。")]

#html.figure(id: "T002", class: "essay-paper-figure")[
  #image("assets/table-13.png")
]

#zh(id: "T002")[#text("抵押贷款、无抵押贷款和粮食贷款最常见的利率（百分比）。各行：旁遮普、联合省、比哈尔、奥里萨、孟加拉、中央省、孟买、信德、马德拉斯。")]

#html.p(id: "en-S050")[#text("This interpretation can be seen in Sir Malcolm Darling's interpretation of the village moneylender's power:")]

#zh(id: "S050")[#text("这种解释可以从马尔科姆·达林爵士对乡村放债人权力的解释中看出：")]

#html.p(id: "en-S051")[#text("It is only fair to remember that in the Indian village the money-lender is often the one thrifty person amongst a generally thriftless people; and that his methods of business, though demoralizing under modern conditions, suit the happy-go-lucky ways of the peasant. He is always accessible, even at night; dispenses with troublesome formalities, asks no inconvenient questions, advances promptly, and if interest is paid, does not press for repayment of principal. He keeps in close personal touch with his clients, and in many villages shares their occasions of weal or woe. With his intimate knowledge of those around him he is able, without serious risk, to finance those who would otherwise get no loan at all. [Italics added.] 8")]

#zh(id: "S051")[#text("公平地记住，在印度村庄，放债人往往是普遍不节俭的人们中唯一节俭的人；他的经营方式虽然在现代条件下令人士气低落，但却适合农民无忧无虑的生活方式。即使在晚上，他也总是很容易接近。免去繁琐的手续，不问不方便的问题，及时垫付，如果支付了利息，也不催促偿还本金。他与客户保持着密切的个人联系，并在许多村庄分享他们的福祸。凭借对周围人的深入了解，他能够在没有严重风险的情况下为那些根本无法获得贷款的人提供资金。 [添加斜体。] 8")]

#html.p(id: "en-S052")[#text("Or look at Barbara Ward's account:")]

#zh(id: "S052")[#text("或者看看 Barbara Ward 的账户：")]

#html.p(id: "en-S053")[#text("A small shopkeeper in a Hong Kong fishing village told me: \"I give credit to anyone who anchors regularly in our bay; but if it is someone I don't know well, then I think twice about it unless I can find out all about him.\"9")]

#zh(id: "S053")[#text("香港渔村的一位小店主告诉我：“我对经常在我们海湾抛锚的人表示信任；但如果是我不熟悉的人，那么我会三思而后行，除非我能了解他的全部情况。”9")]

#html.p(id: "en-S054")[#text("Or, a profitable sideline of cotton ginning in Iran is the loaning of money for the next season, since the ginning companies often have a line of credit from Teheran banks at the market rate of interest. But in the first years of operation large losses are expected from unpaid debts - due to poor knowledge of the local scene.'")]

#zh(id: "S054")[#text("或者，伊朗轧棉业的一项有利可图的副业是为下个季节提供贷款，因为轧棉公司通常以市场利率从德黑兰银行获得信贷额度。但在运营的最初几年，由于对当地情况了解甚少，未偿债务预计会带来巨额损失。")]

== IV. COUNTERACTING INSTITUTIONS / 四．对抗机构

#html.p(id: "en-S055")[#text("Numerous institutions arise to counteract the effects of quality uncertainty. One obvious institution is guarantees. Most consumer durables carry guarantees to ensure the buyer of some normal expected quality. One natural result of our model is that the risk is borne by the seller rather than by the buyer.")]

#zh(id: "S055")[#text("许多机构的出现是为了抵消质量不确定性的影响。一项明显的制度是担保。大多数耐用消费品都有保证，以确保买家获得一些正常的预期质量。我们模型的一个自然结果是风险由卖方而不是买方承担。")]

#html.p(id: "en-S056")[#text("A second example of an institution which counteracts the effects of quality uncertainty is the brand-name good. Brand names")]

#zh(id: "S056")[#text("抵消质量不确定性影响的制度的第二个例子是名牌商品。品牌名称")]

#html.p(id: "en-S057")[#text("8. Darling, op. cit., p. 204.")]

#zh(id: "S057")[#text("8. 亲爱的，同前。引，第。 204.")]

#html.p(id: "en-S058")[#text("not only indicate quality but also give the consumer a means of retaliation if the quality does not meet expectations. For the consumer will then curtail future purchases. Often too, new products are associated with old brand names. This ensures the prospective consumer of the quality of the product.")]

#zh(id: "S058")[#text("不仅表明了质量，而且还为消费者在质量不符合期望时提供了报复的手段。因为消费者将减少未来的购买。新产品也经常与旧品牌联系在一起。这确保了潜在消费者的产品质量。")]

#html.p(id: "en-S059")[#text("Chains - such as hotel chains or restaurant chains - are similar to brand names. One observation consistent with our approach is the chain restaurant. These restaurants, at least in the United States, most often appear on interurban highways. The customers are seldom local. The reason is that these well-known chains offer a better hamburger than the average local restaurant; at the same time, the local customer, who knows his area, can usually choose a place he prefers.")]

#zh(id: "S059")[#text("连锁店 - 例如连锁酒店或连锁餐厅 - 类似于品牌名称。与我们的方法一致的一项观察是连锁餐厅。这些餐馆，至少在美国，最常出现在城际高速公路上。顾客很少是本地人。原因是这些知名连锁店提供的汉堡比当地普通餐馆的汉堡更好；同时，了解自己所在区域的当地客户通常可以选择他喜欢的地方。")]

#html.p(id: "en-S060")[#text("Licensing practices also reduce quality uncertainty. For instance, there is the licensing of doctors, lawyers, and barbers. Most skilled labor carries some certification indicating the attainment of certain levels of proficiency. The high school diploma, the baccalaureate degree, the Ph.D., even the Nobel Prize, to some degree, serve this function of certification. And education and labor markets themselves have their own \"brand names.\"")]

#zh(id: "S060")[#text("许可实践也减少了质量的不确定性。例如，有医生、律师和理发师的执照。大多数熟练工人都持有一些证书，表明已达到一定的熟练程度。高中文凭、学士学位、博士学位，甚至诺贝尔奖，在某种程度上都起到了这种认证的作用。教育和劳动力市场本身也有自己的“品牌”。")]

== V. CONCLUSION / 五、结论

#html.p(id: "en-S061")[#text("We have been discussing economic models in which \"trust\" is important. Informal unwritten guarantees are preconditions for trade and production. Where these guarantees are indefinite, business will suffer -as indicated by our generalized Gresham's law. This aspect of uncertainty has been explored by game theorists, as in the Prisoner's Dilemma, but usually it has not been incorporated in the more traditional Arrow-Debreu approach to uncertainty.2 But the difficulty of distinguishing good quality from bad is inherent in the business world; this may indeed explain many economic institutions and may in fact be one of the more important aspects of uncertainty.")]

#zh(id: "S061")[#text("我们一直在讨论“信任”很重要的经济模型。非正式的不成文保证是贸易和生产的先决条件。如果这些保证是无限期的，企业就会受到影响——正如我们的广义格雷欣定律所表明的那样。博弈论学家已经对这一方面的不确定性进行了探索，例如在囚徒困境中，但通常它没有被纳入更传统的阿罗-德布鲁不确定性方法中。2但是区分好坏质量的困难是商业世界所固有的；这确实可以解释许多经济制度，而且实际上可能是不确定性的更重要方面之一。")]

#html.p(id: "en-S062")[#text("INDIAN STATISTICAL INSTITUTE-PLANNING UNIT,NEW DELHI INDIAN STATISTICAL INSTITUTE -PLANNING UNIT, NEW DELHI")]

#zh(id: "S062")[#text("印度统计局规划单位，新德里 印度统计局规划单位，新德里")]

#html.p(id: "en-S063")[#text("2. R. Radner, \"Equilibre de Marches a Terme et au Comptant en Caa")]

#zh(id: "S063")[#text("2. R. Radner，“Equilibre de Marches a Terme et au Comptant en Caa”")]

== Notes / 笔记

#html.p(id: "en-N001")[#text("*The author would especially like to thank Thomas Rothenberg for invaluable comments and inspiration. In addition he is indebted to Roy Radner, Albert Fishlow, Bernard Saffran, William D. Nordhaus, Giorgio L Malfa, Charles C. Holt, John Letiche, and the referee for help and sugge tions. He would also like to thank the Indian Statistical Institute and t Ford Foundation for financial support.")]

#zh(id: "N001")[#text("*作者特别感谢 Thomas Rothenberg 的宝贵评论和灵感。此外，他还感谢 Roy Radner、Albert Fishlow、Bernard Saffran、William D. Nordhaus、Giorgio L Malfa、Charles C. Holt、John Letiche 以及裁判的帮助和建议。他还要感谢印度统计研究所和福特基金会的财政支持。")]

#html.p(id: "en-N002")[#text("phasizes \"moral hazard\" rather than \"adverse selection.\" In its strict sense, the presence of \"moral hazard\" is equally disadvantageous for both governmental and private programs; in its broader sense, which includes \"adverse selection,\" \"moral hazard\" gives a decided advantage to government insurance programs. 2. 0. D. Dickerson, Health Insurance (Homewood, Ill.: Irwin, 1959), p. 333. 3. 0. W. Anderson (with J. J. Feldman), Family Medical Costs and Insurance (New York: Mc Graw-Hill, 1956). 4. H. S. Denenberg, R. D. Eilers, G. W. Hoffman, C. A. Kline, J. J. Melone, and H. W. Snider, Risk and Insurance (Englewood Cliffs, N. J.: Prentice Hall, 1964), p. 446.")]

#zh(id: "N002")[#text("强调“道德风险”而不是“逆向选择”。从严格意义上讲，“道德风险”的存在对政府和私人项目同样不利；从更广泛的意义上来说，包括“逆向选择”，“道德风险”为政府保险计划带来了决定性的优势。 2. 0. D. Dickerson，《健康保险》（伊利诺伊州霍姆伍德：欧文，1959 年），第 14 页。 333. 3. 0. W. Anderson（与 J. J. Feldman 合作），《家庭医疗费用和保险》（纽约：Mc Graw-Hill，1956 年）。 4. H. S. Denenberg、R. D. Eilers、G. W. Hoffman、C. A. Kline、J. J. Melone 和 H. W. Snider，《风险与保险》（新泽西州恩格尔伍德悬崖：Prentice Hall，1964 年），第 17 页。 446.")]

#html.p(id: "en-N003")[#text("5. The following quote, again taken from an insurance textbook, shows how far the medical insurance market is from perfect competition: is . .insurance companies must screen their applicants. Naturally it is true that many people will voluntarily seek adequate insurance on their own initiative. But in such lines as accident and health insurance, companies are likely to give a second look to persons who voluntarily seek insurance without being approached by an agent.\" (F. J. Angell, Insurance, Principles and Practices, New York: The Ronald Press, 1957, pp. 8-9.) This shows that insurance is not a commodity for sale on the open market. 6. T. W. Schultz, The Economic Value of Education (New York: Columbia University Press, 1964), p. 42.")]

#zh(id: "N003")[#text("5. 下面这句话再次摘自保险教科书，显示了医疗保险市场距离完全竞争还有多远： 是 。 .保险公司必须筛选其申请人。当然，确实有很多人会主动寻求足够的保险。但在事故和健康保险等领域，公司可能会重新审视那些未经代理人联系而自愿寻求保险的人。”（F. J. Angell，《保险、原则和实践》，纽约：罗纳德出版社，1957 年，第 8-9 页。）这表明保险不是在公开市场上出售的商品。 6. T. W. Schultz，《教育的经济价值》（纽约：哥伦比亚大学出版社， 1964 年），第 42 页。")]

#html.p(id: "en-N004")[#text("cal Economy, Vol. 70 (Oct. 1962), Supplement, p. 104.")]

#zh(id: "N004")[#text("加州经济，卷。 70（1962 年 10 月），补编，第 17 页。 104.")]

#html.p(id: "en-N005")[#text("8. The Times of India, Nov. 10, 1967, p. 1. 9. See MI. J. Levy, Jr., \"Contrasting Factors in the Modernization of China and Japan,\" in Economic Growth: Brazil, India, Japan, ed. S. Kuznets, et. al. (Durham, N. C.: Duke University Press, 1955). 1. C. P. Kindleberger, Economic Development (New York: Mc Graw- Hill, 1958), p. 86. 2. For example, see W. Arthur Lewis, The Theory of Economic Growth (Homewood, Ill.: Irwin, 1955), p. 196.")]

#zh(id: "N005")[#text("8. 《印度时报》，1967 年 11 月 10 日，第 17 页1. 9. 参见 MI。 J. Levy, Jr.，“中国和日本现代化的对比因素”，《经济增长：巴西、印度、日本》，编辑。 S.库兹涅茨等。等人。 （北卡罗来纳州达勒姆：杜克大学出版社，1955 年）。 1. C. P. Kindleberger，《经济发展》（纽约：Mc Graw-Hill，1958 年），第 14 页。 86. 2. 例如，参见 W. Arthur Lewis，《经济增长理论》（伊利诺伊州霍姆伍德：欧文，1955 年），第 14 页。 196.")]

#html.p(id: "en-N006")[#text("3. Report of the Committee on the Distribution of Income and Levels of Living, Part I, Government of India, Planning Commission, Feb. 1964, p. 44. 4. H. Tinker, South Asia: A Short History (New York: Praeger, 1966), p. 134. 5. The existence of the following table (and also the small per cent of firms under mixed control) indicates the communal iz ation of the control of firms. Source: M. M. Mehta, Structure of Indian Industries (Bombay: Popular Book Depot, 1955), p. 314. V. B. Singh, editor, Economic History of India, 1857-1956 (Bombay: Allied Publishers, 1965).")]

#zh(id: "N006")[#text("3. 收入分配和生活水平委员会的报告，第一部分，印度政府，计划委员会，1964 年 2 月，第 14 页。 44. 4. H. Tinker，《南亚：简史》（纽约：Praeger，1966 年），第 14 页。 134. 5. 下表的存在（以及混合控制下的一小部分公司）表明公司控制权的公共化。资料来源：M. M. Mehta，《印度工业结构》（孟买：大众书库，1955 年），第 14 页。 314. V. B. Singh，编辑，《印度经济史，1857-1956》（孟买：联合出版社，1965 年）。")]

#html.p(id: "en-N007")[#text("6. For the mixed record of industrial profits, see D. H. Buchanan, The Development of Capitalist Enterprise in India (New York: Kelley, 1966, reprinted). 7. The leading authority on this is Sir Malcolm Darling. See his Punjabi Peasant in Prosperity and Debt. The following table may also prove instructive:")]

#zh(id: "N007")[#text("6. 关于工业利润的好坏记录，参见 D. H. Buchanan，《印度资本主义企业的发展》（纽约：Kelley，1966 年，重印）。 7. 这方面的主要权威是马尔科姆·达林爵士。看看他的《繁荣与债务》中的旁遮普农民。下表也可能具有启发性：")]

#html.p(id: "en-N008")[#text("9. B. Ward, \"Cash or Credit Crops,\" Economic Development and Cultural Change, Vol. 8 (Jan. 1960), reprinted in Peasant Society: A Reader, ed. G. Foster et al. (Boston: Little Brown and Company, 1967). Quote on p. 142. In the same volume, see also G. W. Skinner, \"Marketing and Social Structure in Rural China,\" and S. W. Mintz, \"Pratik: Haitian Personal Economic Relations.\" 1. Personal conversation with mill manager, April 1968.")]

#zh(id: "N008")[#text("9. B. Ward，“现金或信贷作物”，经济发展与文化变革，卷。 8（1960 年 1 月），转载于《农民协会：读者》编辑。 G.福斯特等人。 （波士顿：Little Brown and Company，1967）。引用第 14 页。 142. 在同一卷中，另见 G. W. Skinner，“中国农村的市场营销和社会结构”，以及 S. W. Mintz，“Pratik：海地个人经济关系”。 1. 与工厂经理的私人谈话，1968 年 4 月。")]

#html.p(id: "en-N009")[#text("d'Incertitude,\" in Cahiers d'Econometrie, Vol. 12 (Nov. 1967), Centre National de la Recherche Scientifique, Paris.")]

#zh(id: "N009")[#text("d'Incertitude”，载于 Cahiers d'Econometrie，第 12 卷（1967 年 11 月），巴黎国家科学研究中心。")]
