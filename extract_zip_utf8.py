import os
import zipfile
import shutil
from pathlib import Path
import subprocess
import glob
from datetime import datetime
import re
import jieba
import pypinyin
import json
import yaml
import hashlib
from PIL import Image

def convert_to_english_name(chinese_title):
    """将中文标题转换为规范的英文文件名
    
    Args:
        chinese_title: 中文标题
    
    Returns:
        符合规范的英文文件名：
        1. 使用英文单词
        2. 单词之间用短横线连接
        3. 全部小写
        4. 避免特殊字符
    """
    # 预定义的中文词语映射表
    word_mapping = {
        "回顾": "recap",
        "总结": "recap",
        "月": "month",
        "以前": "before",
        "超过": "over",
        "公里": "kilometers",
        "华南": "south-china",
        "自驾": "road-trip",
        "写一写感受": "review",
        "感受": "review",
        "朝鲜": "north-korea",
        "四日": "four-days",
        "行纪录": "journey",
        "行": "journey",
        "纪录": "record",
        "回忆": "recap",
        "玩具": "toys",
        "游记": "journey",
        "总结": "summary",
        "日记": "diary",
        "体验": "experience",
        "评测": "review",
        "教程": "tutorial",
        "指南": "guide",
        "旅行": "travel",
        "游记": "travel-notes",
        "记录": "record",
        "探索": "explore",
        "观察": "observation",
        "思考": "thoughts",
        "分享": "sharing",
        "生活": "life",
        "工作": "work",
        "学习": "study",
        "随笔": "essay",
        "札记": "notes",
        "小记": "notes",
        "笔记": "notes",
        "感想": "thoughts",
        "心得": "insights",
        "南": "south",
        "北": "north",
        "东": "east",
        "西": "west",
        "中": "central",
        "一": "one",
        "二": "two",
        "三": "three",
        "四": "four",
        "五": "five",
        "六": "six",
        "七": "seven",
        "八": "eight",
        "九": "nine",
        "十": "ten",
        "年": "year",
        "月": "month",
        "日": "day",
        "周": "week",
        "天": "day",
        "时": "hour",
        "分": "minute",
        "秒": "second",
        "上": "up",
        "下": "down",
        "左": "left",
        "右": "right",
        "前": "front",
        "后": "back",
        "里": "inside",
        "外": "outside",
        "大": "big",
        "小": "small",
        "多": "many",
        "少": "few",
        "新": "new",
        "旧": "old",
        "好": "good",
        "坏": "bad",
        "快": "fast",
        "慢": "slow",
        "高": "high",
        "低": "low",
        "远": "far",
        "近": "near",
        "深": "deep",
        "浅": "shallow",
        "轻": "light",
        "重": "heavy",
        "软": "soft",
        "硬": "hard",
        "冷": "cold",
        "热": "hot",
        "干": "dry",
        "湿": "wet",
        "亮": "bright",
        "暗": "dark",
        "静": "quiet",
        "动": "move",
        "开": "open",
        "关": "close",
        "来": "come",
        "去": "go",
        "停": "stop",
        "走": "walk",
        "跑": "run",
        "跳": "jump",
        "看": "look",
        "听": "listen",
        "说": "speak",
        "想": "think",
        "做": "do",
        "用": "use",
        "要": "want",
        "给": "give",
        "找": "find",
        "买": "buy",
        "卖": "sell",
        "学": "learn",
        "教": "teach",
        "问": "ask",
        "答": "answer",
        "笑": "laugh",
        "哭": "cry",
        "玩": "play",
        "工作": "work",
        "休息": "rest",
        "睡觉": "sleep",
        "起床": "wake",
        "吃饭": "eat",
        "喝水": "drink",
        "说话": "talk",
        "走路": "walk",
        "跑步": "run",
        "跳舞": "dance",
        "唱歌": "sing",
        "画画": "draw",
        "写字": "write",
        "读书": "read",
        "游泳": "swim",
        "运动": "exercise",
        "旅游": "travel",
        "购物": "shop",
        "工作": "work",
        "学习": "study",
        "思考": "think",
        "计划": "plan",
        "准备": "prepare",
        "开始": "start",
        "结束": "end",
        "完成": "finish",
        "继续": "continue",
        "等待": "wait",
        "改变": "change",
        "发展": "develop",
        "成长": "grow",
        "创造": "create",
        "建设": "build",
        "保护": "protect",
        "破坏": "destroy",
        "修理": "repair",
        "清洁": "clean",
        "整理": "organize",
        "分析": "analyze",
        "研究": "research",
        "实验": "experiment",
        "测试": "test",
        "检查": "check",
        "观察": "observe",
        "记录": "record",
        "报告": "report",
        "总结": "summarize",
        "评价": "evaluate",
        "判断": "judge",
        "决定": "decide",
        "选择": "choose",
        "推荐": "recommend",
        "建议": "suggest",
        "帮助": "help",
        "支持": "support",
        "反对": "oppose",
        "拒绝": "refuse",
        "接受": "accept",
        "同意": "agree",
        "反对": "disagree",
        "批评": "criticize",
        "表扬": "praise",
        "鼓励": "encourage",
        "安慰": "comfort",
        "关心": "care",
        "爱护": "cherish",
        "保护": "protect",
        "照顾": "take-care",
        "帮忙": "help",
        "服务": "serve",
        "管理": "manage",
        "领导": "lead",
        "指导": "guide",
        "教育": "educate",
        "培训": "train",
        "学习": "learn",
        "研究": "research",
        "发现": "discover",
        "创新": "innovate",
        "改革": "reform",
        "发展": "develop",
        "进步": "progress",
        "提高": "improve",
        "降低": "reduce",
        "增加": "increase",
        "减少": "decrease",
        "扩大": "expand",
        "缩小": "shrink",
        "加强": "strengthen",
        "削弱": "weaken",
        "提升": "enhance",
        "下降": "decline",
        "上升": "rise",
        "成功": "succeed",
        "失败": "fail",
        "胜利": "win",
        "失败": "lose",
        "开始": "begin",
        "结束": "end",
        "继续": "continue",
        "停止": "stop",
        "暂停": "pause",
        "恢复": "resume",
        "重复": "repeat",
        "更新": "update",
        "升级": "upgrade",
        "降级": "downgrade",
        "安装": "install",
        "卸载": "uninstall",
        "配置": "configure",
        "设置": "set",
        "重置": "reset",
        "备份": "backup",
        "恢复": "restore",
        "导入": "import",
        "导出": "export",
        "复制": "copy",
        "粘贴": "paste",
        "剪切": "cut",
        "删除": "delete",
        "移动": "move",
        "重命名": "rename",
        "搜索": "search",
        "查找": "find",
        "替换": "replace",
        "过滤": "filter",
        "排序": "sort",
        "分组": "group",
        "合并": "merge",
        "分割": "split",
        "压缩": "compress",
        "解压": "extract",
        "加密": "encrypt",
        "解密": "decrypt",
        "编码": "encode",
        "解码": "decode",
        "编译": "compile",
        "调试": "debug",
        "测试": "test",
        "部署": "deploy",
        "发布": "publish",
        "订阅": "subscribe",
        "取消订阅": "unsubscribe",
        "注册": "register",
        "登录": "login",
        "注销": "logout",
        "验证": "verify",
        "授权": "authorize",
        "认证": "authenticate",
        "审核": "review",
        "批准": "approve",
        "拒绝": "reject",
        "确认": "confirm",
        "取消": "cancel",
        "提交": "submit",
        "保存": "save",
        "加载": "load",
        "刷新": "refresh",
        "重新加载": "reload",
        "同步": "sync",
        "异步": "async",
        "并行": "parallel",
        "串行": "serial",
        "本地": "local",
        "远程": "remote",
        "在线": "online",
        "离线": "offline",
        "自动": "auto",
        "手动": "manual",
        "默认": "default",
        "自定义": "custom",
        "随机": "random",
        "顺序": "sequence",
        "循环": "loop",
        "递归": "recursive",
        "迭代": "iterate",
        "遍历": "traverse",
        "过滤": "filter",
        "映射": "map",
        "归约": "reduce",
        "聚合": "aggregate",
        "分组": "group",
        "排序": "sort",
        "查询": "query",
        "统计": "statistics",
        "分析": "analysis",
        "监控": "monitor",
        "警告": "alert",
        "错误": "error",
        "异常": "exception",
        "调试": "debug",
        "跟踪": "trace",
        "日志": "log",
        "报告": "report",
        "文档": "document",
        "注释": "comment",
        "说明": "description",
        "示例": "example",
        "模板": "template",
        "样式": "style",
        "主题": "theme",
        "布局": "layout",
        "设计": "design",
        "开发": "develop",
        "测试": "test",
        "生产": "production",
        "维护": "maintain",
        "支持": "support",
        "服务": "service",
        "系统": "system",
        "网络": "network",
        "数据库": "database",
        "服务器": "server",
        "客户端": "client",
        "前端": "frontend",
        "后端": "backend",
        "接口": "interface",
        "协议": "protocol",
        "算法": "algorithm",
        "架构": "architecture",
        "框架": "framework",
        "模块": "module",
        "组件": "component",
        "插件": "plugin",
        "扩展": "extension",
        "工具": "tool",
        "库": "library",
        "包": "package",
        "依赖": "dependency",
        "版本": "version",
        "更新": "update",
        "升级": "upgrade",
        "补丁": "patch",
        "修复": "fix",
        "漏洞": "vulnerability",
        "安全": "security",
        "性能": "performance",
        "优化": "optimization",
        "效率": "efficiency",
        "质量": "quality",
        "可靠性": "reliability",
        "稳定性": "stability",
        "可用性": "availability",
        "可扩展性": "scalability",
        "可维护性": "maintainability",
        "兼容性": "compatibility",
        "互操作性": "interoperability",
        "标准化": "standardization",
        "规范化": "normalization",
        "模块化": "modularization",
        "自动化": "automation",
        "智能化": "intelligence",
        "数字化": "digitalization",
        "信息化": "informatization",
        "现代化": "modernization",
        "全球化": "globalization",
        "本地化": "localization",
        "国际化": "internationalization",
        "产业化": "industrialization",
        "商业化": "commercialization",
        "专业化": "specialization",
        "简单化": "simplification",
        "复杂化": "complication",
        "多样化": "diversification",
        "统一化": "unification",
        "集中化": "centralization",
        "分散化": "decentralization",
        "系统化": "systematization",
        "结构化": "structuralization",
        "正常化": "normalization",
        "合理化": "rationalization",
        "优质化": "qualification",
        "精细化": "refinement",
        "深入化": "deepening",
        "广泛化": "generalization",
        "普及化": "popularization",
        "科学化": "scientification",
        "规范化": "standardization",
        "制度化": "institutionalization",
        "法制化": "legalization",
        "正规化": "formalization",
        "专门化": "specialization",
        "职业化": "professionalization",
        "产业化": "industrialization",
        "市场化": "marketization",
        "社会化": "socialization",
        "现实化": "realization",
        "理想化": "idealization",
        "具体化": "concretization",
        "抽象化": "abstraction",
        "形象化": "visualization",
        "数字化": "digitization",
        "电子化": "electronization",
        "网络化": "networking",
        "信息化": "informatization",
        "智能化": "intelligentization",
        "自动化": "automation",
        "机械化": "mechanization",
        "工业化": "industrialization",
        "现代化": "modernization",
        "标准化": "standardization",
        "规范化": "normalization",
        "系统化": "systematization",
        "程序化": "programming",
        "模块化": "modularization",
        "结构化": "structuring",
        "层次化": "hierarchization",
        "序列化": "serialization",
        "并行化": "parallelization",
        "优化": "optimization",
        "简化": "simplification",
        "净化": "purification",
        "美化": "beautification",
        "绿化": "greening",
        "净化": "purification",
        "强化": "strengthening",
        "弱化": "weakening",
        "软化": "softening",
        "硬化": "hardening",
        "深化": "deepening",
        "淡化": "dilution",
        "固化": "solidification",
        "液化": "liquefaction",
        "气化": "gasification",
        "净化": "purification",
        "同化": "assimilation",
        "异化": "alienation",
        "进化": "evolution",
        "退化": "degeneration",
        "变化": "change",
        "转化": "transformation",
        "溶化": "dissolution",
        "分化": "differentiation",
        "融化": "melting",
        "汽化": "vaporization",
        "结晶化": "crystallization",
        "中性化": "neutralization",
        "正常化": "normalization",
        "理想化": "idealization",
        "现实化": "realization",
        "具体化": "concretization",
        "抽象化": "abstraction",
        "形象化": "visualization",
        "立体化": "stereoscopic",
        "平面化": "planarization",
        "数量化": "quantification",
        "质量化": "qualification",
        "价值化": "valorization",
        "商品化": "commodification",
        "货币化": "monetization",
        "资本化": "capitalization",
        "产业化": "industrialization",
        "企业化": "enterprization",
        "公司化": "corporatization",
        "集团化": "grouping",
        "品牌化": "branding",
        "连锁化": "chaining",
        "规模化": "scaling",
        "标准化": "standardization",
        "规范化": "normalization",
        "正规化": "regularization",
        "制度化": "institutionalization",
        "法制化": "legalization",
        "系统化": "systematization",
        "程序化": "programming",
        "模块化": "modularization",
        "结构化": "structuring",
        "层次化": "hierarchization",
        "序列化": "serialization",
        "并行化": "parallelization",
        "网络化": "networking",
        "信息化": "informatization",
        "数字化": "digitization",
        "电子化": "electronization",
        "智能化": "intelligentization",
        "自动化": "automation",
        "机械化": "mechanization",
        "工业化": "industrialization",
        "现代化": "modernization",
        "全球化": "globalization",
        "国际化": "internationalization",
        "本地化": "localization",
        "区域化": "regionalization",
        "城市化": "urbanization",
        "郊区化": "suburbanization",
        "农村化": "ruralization",
        "工业化": "industrialization",
        "商业化": "commercialization",
        "市场化": "marketization",
        "民营化": "privatization",
        "私有化": "privatization",
        "公有化": "nationalization",
        "集体化": "collectivization",
        "社会化": "socialization",
        "大众化": "popularization",
        "普及化": "universalization",
        "专业化": "specialization",
        "职业化": "professionalization",
        "学术化": "academization",
        "科学化": "scientification",
        "理论化": "theorization",
        "实践化": "practicalization",
        "生活化": "lifestyling",
        "日常化": "routinization",
        "习惯化": "habituation",
        "正常化": "normalization",
        "异常化": "abnormalization",
        "特殊化": "specialization",
        "普遍化": "generalization",
        "一般化": "generalization",
        "具体化": "concretization",
        "抽象化": "abstraction",
        "形象化": "visualization",
        "直观化": "intuitionalization",
        "感性化": "sensibilization",
        "理性化": "rationalization",
        "主观化": "subjectivization",
        "客观化": "objectivization",
        "理想化": "idealization",
        "现实化": "realization",
        "虚拟化": "virtualization",
        "真实化": "realization",
        "具象化": "concretization",
        "意象化": "imagization",
        "符号化": "symbolization",
        "数字化": "digitization",
        "模型化": "modeling",
        "程序化": "programming",
        "系统化": "systematization",
        "结构化": "structuring",
        "条理化": "organization",
        "规范化": "standardization",
        "标准化": "standardization",
        "正规化": "regularization",
        "制度化": "institutionalization",
        "法制化": "legalization",
        "规则化": "regularization",
        "秩序化": "ordering",
        "组织化": "organization",
        "管理化": "management",
        "控制化": "control",
        "监督化": "supervision",
        "指导化": "guidance",
        "引导化": "guidance",
        "教育化": "education",
        "培训化": "training",
        "学习化": "learning",
        "研究化": "research",
        "探索化": "exploration",
        "发现化": "discovery",
        "创新化": "innovation",
        "发明化": "invention",
        "创造化": "creation",
        "建设化": "construction",
        "发展化": "development",
        "改革化": "reform",
        "革新化": "renovation",
        "更新化": "renewal",
        "改进化": "improvement",
        "提高化": "enhancement",
        "升级化": "upgrade",
        "进步化": "progress",
        "先进化": "advancement",
        "现代化": "modernization",
        "未来化": "futurization"
    }
    
    # 1. 分词
    words = jieba.cut(chinese_title)
    
    # 2. 转换每个词
    english_words = []
    for word in words:
        # 检查是否在映射表中
        if word in word_mapping:
            english_words.append(word_mapping[word])
        else:
            # 如果不在映射表中，转换为拼音
            pinyin = pypinyin.lazy_pinyin(word)
            english_words.extend(pinyin)
    
    # 3. 处理英文单词
    # 移除所有非字母数字的字符
    english_words = [re.sub(r'[^a-zA-Z0-9]', '', word) for word in english_words]
    # 移除空字符串和特殊字符
    english_words = [word for word in english_words if word and word not in ["s", "S"]]
    
    # 4. 组合成文件名
    filename = '-'.join(english_words).lower()
    
    # 5. 清理多余的短横线
    filename = re.sub(r'-+', '-', filename)  # 将多个连续的短横线替换为单个
    filename = filename.strip('-')  # 移除首尾的短横线
    
    return filename

def generate_frontmatter(title, description="", tags=None):
    """生成符合规范的 Front Matter
    
    Args:
        title: 文章标题
        description: 文章描述
        tags: 标签列表
    
    Returns:
        格式化的 Front Matter 字符串
    """
    if tags is None:
        tags = []
    
    # 按照规范的顺序创建 frontmatter
    frontmatter = {
        "author": "Joe",  # YAML 会自动处理引号
        "date": datetime.now().strftime("%Y-%m-%d"),
        "description": description,
        "draft": False,
        "tags": tags,
        "title": title
    }
    
    # 使用 yaml 模块生成格式化的 Front Matter
    # default_style='\"' 确保字符串使用双引号
    # sort_keys=False 保持字段顺序
    return "---\n" + yaml.dump(frontmatter, 
                              allow_unicode=True,
                              default_flow_style=False,
                              sort_keys=False,
                              default_style='\"') + "---\n\n"

def extract_date_from_content(content):
    """从文章内容中提取日期
    
    Args:
        content: 文章内容
    
    Returns:
        datetime 对象
    """
    # 1. 尝试从 Front Matter 中提取
    front_matter_match = re.search(r'date:\s*[\'"]?(\d{4}-\d{1,2}-\d{1,2})[\'"]?', content)
    if front_matter_match:
        try:
            date_str = front_matter_match.group(1)
            return datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            pass
    
    # 2. 尝试从文章内容中提取年份和月份
    year_match = re.search(r'(\d{4})年', content)
    month_match = re.search(r'(\d{1,2})月', content)
    
    if year_match and month_match:
        year = int(year_match.group(1))
        month = int(month_match.group(1))
        return datetime(year, month, 1)
    
    # 3. 如果都没找到，返回当前日期
    return datetime.now()

def process_content(content, article_name):
    """处理文章内容，移除重复标题和处理链接
    
    Args:
        content: 原始文章内容
        article_name: 文章英文名称
    
    Returns:
        处理后的文章内容
    """
    lines = content.split('\n')
    
    # 移除开头的标题（# 开头的行）
    if lines and lines[0].strip().startswith('# '):
        lines = lines[1:]
    
    # 处理 Notion 链接
    processed_lines = []
    for line in lines:
        # 1. 替换 Notion 链接为内部链接
        line = re.sub(
            r'\[([^\]]+)\]\(https://www\.notion\.so/[^)]+\)',
            lambda m: f'[{m.group(1)}](/posts/{convert_to_english_name(m.group(1))})',
            line
        )
        
        # 2. 移除 Notion 页面 ID
        line = re.sub(r'\?pvs=\d+', '', line)
        
        processed_lines.append(line)
    
    # 确保段落之间有正确的空行
    content = '\n'.join(processed_lines).strip()
    return content + '\n'

def process_image_links(content, article_name):
    """处理文章中的图片链接
    
    Args:
        content: 文章内容
        article_name: 文章英文名称
    
    Returns:
        处理后的文章内容
    """
    # 替换图片链接
    # 1. 替换完整的 Notion 图片路径
    content = re.sub(
        r'!\[(.*?)\]\((.*?)(?:Untitled.*?\.png|.*?\.(png|jpg|jpeg|gif))\)',
        lambda m: f'![{m.group(1)}](/images/posts/{article_name}/image-{abs(hash(m.group(2)))}.webp)',
        content
    )
    
    # 2. 替换相对路径的图片链接
    content = re.sub(
        r'!\[(.*?)\]\((?!http|/)(.*?)(?:Untitled.*?\.png|.*?\.(png|jpg|jpeg|gif))\)',
        lambda m: f'![{m.group(1)}](/images/posts/{article_name}/image-{abs(hash(m.group(2)))}.webp)',
        content
    )
    
    return content

def extract_zip_utf8(zip_path="Notionfiles"):
    """解压并处理 Notion 导出的 ZIP 文件
    
    Args:
        zip_path: ZIP 文件所在目录
    """
    # 创建临时目录
    temp_dir = "temp_notion"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    
    # 查找 ZIP 文件
    zip_files = [f for f in os.listdir(zip_path) if f.endswith('.zip')]
    if not zip_files:
        print("未找到 ZIP 文件")
        return
    
    for zip_file in zip_files:
        full_path = os.path.join(zip_path, zip_file)
        print(f"正在解压文件: {full_path}")
        
        try:
            with zipfile.ZipFile(full_path, 'r') as zip_ref:
                # 解压所有文件
                for file_info in zip_ref.filelist:
                    try:
                        # 使用 CP437 编码处理文件名
                        file_name = file_info.filename.encode('cp437').decode('utf-8')
                    except:
                        # 如果转换失败，尝试直接使用原始文件名
                        file_name = file_info.filename
                    
                    # 创建目标路径
                    target_path = os.path.join(temp_dir, file_name)
                    
                    # 确保目标目录存在
                    os.makedirs(os.path.dirname(target_path), exist_ok=True)
                    
                    # 解压文件
                    try:
                        source = zip_ref.open(file_info)
                        target = open(target_path, "wb")
                        with source, target:
                            shutil.copyfileobj(source, target)
                        print(f"成功提取: {file_name}")
                    except Exception as e:
                        print(f"提取文件失败: {file_name}")
                        print(f"错误信息: {str(e)}")
                        continue
                
                # 处理所有 Markdown 文件
                for root, dirs, files in os.walk(temp_dir):
                    for file in files:
                        if file.endswith('.md'):
                            md_path = os.path.join(root, file)
                            
                            # 读取文件内容
                            try:
                                with open(md_path, 'r', encoding='utf-8') as f:
                                    content = f.read()
                                    
                                    # 提取标题
                                    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
                                    if title_match:
                                        title = title_match.group(1)
                                    else:
                                        title = os.path.splitext(file)[0]
                                    
                                    # 提取描述（第一段非空文本）
                                    description = ""
                                    for line in content.split('\n'):
                                        line = line.strip()
                                        if line and not line.startswith('#'):
                                            description = line
                                            break
                                    
                                    # 提取文章日期
                                    article_date = extract_date_from_content(content)
                                    
                                    # 生成英文文件名
                                    article_name = convert_to_english_name(title)
                                    
                                    # 处理文章内容（移除重复标题和处理链接）
                                    processed_content = process_content(content, article_name)
                                    
                                    # 处理图片链接
                                    processed_content = process_image_links(processed_content, article_name)
                                    
                                    # 生成 Front Matter
                                    front_matter = generate_frontmatter(
                                        title=title,
                                        description=description,
                                        tags=[]  # 这里可以添加标签提取逻辑
                                    )
                                    
                                    # 组合最终内容
                                    final_content = front_matter + processed_content
                                    
                                    # 保存处理后的文件
                                    output_path = f"content/posts/{article_name}.md"
                                    os.makedirs(os.path.dirname(output_path), exist_ok=True)
                                    with open(output_path, 'w', encoding='utf-8') as f:
                                        f.write(final_content)
                                    
                                    print(f"\n处理文章: {title} -> {article_name}")
                                    
                                    # 处理图片
                                    try:
                                        subprocess.run(['python', 'process_notion_links.py',
                                                     article_name, '--input', md_path],
                                                     check=True)
                                    except subprocess.CalledProcessError as e:
                                        print(f"处理文章失败: {str(e)}")
                                        continue
                                    
                            except Exception as e:
                                print(f"处理文件失败: {str(e)}")
                                continue
        
        except Exception as e:
            print(f"处理 ZIP 文件时出错: {str(e)}")
            continue
    
    print("\n解压和基础处理完成！")

if __name__ == "__main__":
    extract_zip_utf8() 