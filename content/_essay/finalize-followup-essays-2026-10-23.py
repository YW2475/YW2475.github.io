"""Apply source paragraph repair and a limited, explicit translation spot review."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
manual = {
    'langmuir-pathological': {
        'S001': '这是欧文·朗缪尔在1954年3月8日录下的内容，根据我于1953年12月18日所作《病态科学》演讲录音带的第三部分转录而成。',
        'S002': '戴维斯–巴恩斯效应',
        'S042': 'N射线',
        'S054': '有丝分裂辐射',
        'S058': '病态科学的典型症状',
        'S061': '表一',
        'S062': '病态科学的症状：',
        'S063': '1. 所观察到的最大效应，由强度刚刚达到可检测程度的作用源产生；而效应的大小，基本不随作用源的强度而改变。',
        'S064': '2. 效应的大小始终接近检测极限；或者，因为结果的统计显著性很低，必须进行大量测量。',
        'S065': '3. 声称具有极高的精确度。',
        'S066': '4. 提出与经验相悖的离奇理论。',
        'S067': '5. 面对批评，总是以临时想出的特设借口来应付。',
        'S068': '6. 支持者与批评者之比上升到约50%，随后逐渐下降，直至无人问津。',
        'S069': '所观察到的最大效应，是由强度刚刚达到可检测程度的作用源产生的。举例说，如果一个洋葱根能通过紫外线影响另一个洋葱根，你可能会想，换用紫外线光源，效果岂不是应当更好？哦，不！绝对不！强度必须恰好就是一个洋葱根发出的那么大。十个洋葱根也不会比一个更有效，而且与作用源的距离毫无关系。它不遵循反平方定律，也不遵循任何这么简单的规律。换句话说，效应与作用源的强度无关。有丝分裂辐射是这样，N射线也是这样。十块砖与一块砖产生的效应并无差别。强度必须很低。我们知道为什么必须低：这样你才容易欺骗自己，否则它就不灵了。戴维斯–巴恩斯效应在灯丝关闭时同样存在。他们照样数出了闪烁。',
        'S078': '阿利森效应',
        'S091': '超感官知觉',
        'S114': '飞碟',
        'S119': '提问环节',
        'S136': '（怀特）：据我记忆，这是我们开过的持续时间最久的一次讨论会。能够请到这样一位演讲者，是莫大的荣幸。谢谢您，朗缪尔博士。',
    },
    'russell-rubbish': {
        'S001': '人是理性的动物——至少别人是这么告诉我的。在漫长的一生中，我一直认真寻找支持这个说法的证据；尽管找遍了横跨三大洲的许多国家，至今却还没有这份好运。相反，我看见世界不断陷入更深的疯狂。我看见那些曾经引领文明的伟大民族，被鼓吹浮夸谬论的人带上歧途。我看见残酷、迫害和迷信日益猖獗，几乎到了这样的地步：赞美理性，反倒会使人被看作一个从逝去时代侥幸活到今天、不合时宜的老古董。这一切令人沮丧，可是忧郁无济于事。为了摆脱它，我不得不比从前更用心地研究过去，结果发现，正如伊拉斯谟所发现的那样，愚蠢历久不衰，人类却仍然生存了下来。把我们时代的愚行放在过去的愚行中看，就容易忍受一些。下面，我会把今天的蠢事与往昔的蠢事穿插起来。这样做，也许有助于我们看清自己所处时代的位置，并认识到：它并不比祖先们经历过、而终于没有遭到毁灭的那些时代糟糕多少。',
        'S098': '如果这些信念全被冷冰冰的科学取代，世界也许会失去一些趣味和多样性。或许我们不妨为所谓的“字母派”感到高兴：他们之所以得了这个名字，是因为他们排斥一切世俗学问，连学习字母ABC也视为罪恶。我们也可以欣赏那位南美耶稣会士的困惑：洪水以后，树懒究竟怎样一路从阿拉拉特山走到了秘鲁？它行动如此迟缓，这段旅程实在几乎令人难以置信。明智的人会享用供应充足的好东西；至于智识垃圾，无论在我们这个时代，还是在任何别的时代，他都会发现食粮丰盛。',
    },
}
record = {}
for ident, overrides in manual.items():
    path = ROOT / 'readers' / ident / 'source_map.json'
    data = json.loads(path.read_text(encoding='utf-8'))
    blocks = data['blocks']
    if ident == 'langmuir-pathological':
        first = next(i for i, b in enumerate(blocks) if b['id'] == 'S069')
        if blocks[first + 1]['id'] == 'S070':
            old = blocks[first:first + 4]
            assert [b['id'] for b in old] == ['S069', 'S070', 'S071', 'S072']
            merged = dict(old[0], en=' '.join(b['en'] for b in old).replace(' .', '.'),
                          zh=''.join(b['zh'] for b in old),
                          repaired_source_block_ids=[b['id'] for b in old])
            blocks[first:first + 4] = [merged]
    corrections = {}
    for i, b in enumerate(blocks):
        b['order'] = i
        if b['id'] in overrides:
            b['zh'] = overrides[b['id']]
            b['translation_method'] = 'assistant translated or retranscribed during limited source review'
            key = hashlib.sha256(b['en'].encode()).hexdigest()
            corrections[key] = dict(source_id=b['id'], zh=b['zh'])
        elif ident == 'langmuir-pathological':
            for old, new in {'病理科学': '病态科学', '病理学科学': '病态科学',
                             '丝裂原射线': '有丝分裂辐射', '致变射线': '有丝分裂辐射',
                             '有丝分裂射线': '有丝分裂辐射', '艾莉森': '阿利森'}.items():
                b['zh'] = b.get('zh', '').replace(old, new)
            if 'statistical significance' in b['en'].lower():
                b['zh'] = b['zh'].replace('统计意义', '统计显著性')
        if ident == 'russell-rubbish':
            b['zh'] = b['zh'].replace('纳粹的阶级和档案', '纳粹的普通成员').replace('知识垃圾', '智识垃圾')
    data['coverage'].update(blocks=len(blocks), source_characters=sum(len(b['en']) for b in blocks))
    data['translation_status'] = 'complete paragraph coverage; machine draft with selected direct translations and terminology corrections; limited spot review'
    data['translation_review'] = dict(date='2026-10-23', scope='First/last paragraphs, section headings, six symptoms, one repaired paragraph and recurring terms; not a complete literary or technical edit.')
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    record[ident] = corrections
    print(f'{ident}: {len(blocks)} aligned blocks, {len(corrections)} explicit reviewed translations')
(ROOT / 'followup-translation-overrides-2026-10-23.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
