#encoding=utf-8
import jieba

seg_list = jieba.cut("我来到清华大学附属中学", cut_all=True)
print("Full Mode:", "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut("我来到清华附中", cut_all=False)
print("Default Mode:", "/ ".join(seg_list))  # 精确模式

seg_list = jieba.cut("Circuitcoder学长太强了！")  # 默认是精确模式
print("/ ".join(seg_list))

seg_list = jieba.cut_for_search("Circuitcoder学长在清华大学计算机系，我们瑟瑟发抖")  # 搜索引擎模式
print("/ ".join(seg_list))
