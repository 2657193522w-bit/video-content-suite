#!/usr/bin/env python3
"""
标题优化模块

功能：
- 基于平台算法优化标题
- 生成SEO友好的标签
- 提供多种标题风格（悬念型、数字型、痛点型等）
- 支持抖音、B站、小红书等平台差异化策略

使用方法：
    python title_optimizer.py --topic "时间管理" --platform 抖音 --count 10
    python title_optimizer.py --topic "AI工具" --platform B站 --style 数字型
"""

import json
import argparse
import random
from typing import List, Dict, Optional


class TitleOptimizer:
    """标题优化器"""
    
    # 标题公式库
    TITLE_FORMULAS = {
        "悬念型": {
            "抖音": [
                "看完这个，我再也不{痛点}了",
                "99%的人都不知道{话题}的真相",
                "{话题}的秘密，今天终于说出来了",
                "原来{话题}才是{收益}的关键",
                "如果你{痛点}，一定要看完这个",
                "{话题}，你可能一直做错了",
                "我发现了一个{话题}的惊人秘密",
                "关于{话题}，专家不会告诉你的事"
            ],
            "B站": [
                "关于{话题}，我发现了一个细思极恐的真相",
                "这可能是全网最详细的{话题}解析",
                "{话题}：一个被误解了{数字}年的概念",
                "深度揭秘：{话题}背后的真相",
                "为什么{话题}比你想象的更重要",
                "关于{话题}，我们都被骗了"
            ],
            "小红书": [
                "后悔没早点知道{话题}！",
                "{话题}的真相，姐妹们一定要知道",
                "原来{话题}这么简单，我之前都错了",
                "{话题}的坑，我帮你踩过了",
                "关于{话题}，我想说的都在这了"
            ]
        },
        "数字型": {
            "抖音": [
                "{数字}个技巧，让你{收益}",
                "{话题}，只需要{数字}分钟",
                "{数字}个{话题}神器，建议收藏",
                "学会这{数字}招，{收益}很简单",
                "{数字}个{话题}误区，你中了几个",
                "{数字}分钟学会{话题}，新手必看"
            ],
            "B站": [
                "{数字}分钟带你了解{话题}",
                "{话题}的{数字}个层次，你在哪一层",
                "我花了{数字}小时总结的{话题}经验",
                "{数字}个{话题}技巧，最后一个最关键",
                "关于{话题}的{数字}个真相"
            ],
            "小红书": [
                "{数字}个{话题}小技巧，建议收藏",
                "亲测！{数字}个{话题}好物分享",
                "{话题}的{数字}个步骤，超简单",
                "{数字}个{话题}误区，别再踩坑了",
                "{数字}分钟搞定{话题}，懒人必看"
            ]
        },
        "痛点型": {
            "抖音": [
                "为什么你总是{痛点}？",
                "{痛点}的解决方案，终于找到了",
                "如果你{痛点}，试试这个方法",
                "{痛点}？那是你没掌握{话题}",
                "解决{痛点}，只需要这{数字}步",
                "{痛点}的救星来了"
            ],
            "B站": [
                "为什么{痛点}？深度解析{话题}",
                "{痛点}的本质原因，终于找到了",
                "从{痛点}到{收益}，我的{话题}之路",
                "{痛点}？那是你理解错了{话题}",
                "彻底解决{痛点}的{话题}方法论"
            ],
            "小红书": [
                "{痛点}的姐妹看过来！",
                "解决{痛点}，亲测有效的方法",
                "{痛点}？试试这个宝藏方法",
                "从{痛点}到{收益}，我只用了{数字}天",
                "{痛点}的终结者，就是这个"
            ]
        },
        "反常识型": {
            "抖音": [
                "专家不会告诉你的{话题}真相",
                "{话题}其实是个骗局？",
                "我反对所有人对{话题}的看法",
                "{话题}，越努力越失败？",
                "关于{话题}，我们都理解错了",
                "{话题}：少即是多"
            ],
            "B站": [
                "{话题}：一个被过度神话的概念",
                "为什么{话题}可能害了你",
                "{话题}的真相：没那么复杂",
                "关于{话题}，我和主流观点不一样",
                "{话题}：是时候说出真相了"
            ],
            "小红书": [
                "{话题}，其实没那么难",
                "别再被{话题}骗了！",
                "{话题}的真相，打破你的认知",
                "关于{话题}，我想唱个反调",
                "{话题}，越简单越有效"
            ]
        },
        "教程型": {
            "抖音": [
                "手把手教你{话题}",
                "{话题}入门指南，新手必看",
                "{数字}步学会{话题}，超简单",
                "{话题}教程：从0到1",
                "一分钟学会{话题}"
            ],
            "B站": [
                "【教程】从零开始学习{话题}",
                "{话题}完全指南：新手到精通",
                "{话题}实战教程：{数字}个案例",
                "系统学习{话题}的方法论",
                "{话题}：一个视频讲清楚"
            ],
            "小红书": [
                "{话题}教程，超详细步骤",
                "手把手教你{话题}，有手就会",
                "{话题}入门，看这一篇就够了",
                "{数字}步搞定{话题}，建议收藏",
                "{话题}攻略，亲测有效"
            ]
        }
    }
    
    # 平台标签推荐
    PLATFORM_TAGS = {
        "抖音": {
            "通用": ["#干货分享", "#知识", "#涨知识", "#科普", "#学习"],
            "科技": ["#科技", "#AI", "#人工智能", "#数码", "#科技改变生活"],
            "生活": ["#生活", "#日常", "#vlog", "#生活方式", "#生活小技巧"],
            "职场": ["#职场", "#打工人", "#职场干货", "#升职加薪", "#面试技巧"],
            "美食": ["#美食", "#美食教程", "#家常菜", "#吃货", "#美食分享"],
            "情感": ["#情感", "#恋爱", "#爱情", "#情感共鸣", "#人间清醒"]
        },
        "B站": {
            "通用": ["知识", "学习", "干货", "教程", "分享"],
            "科技": ["科技", "数码", "AI", "人工智能", "科技数码"],
            "生活": ["生活", "日常", "vlog", "生活方式", "记录"],
            "职场": ["职场", "工作", "求职", "面试", "职业规划"],
            "美食": ["美食", "料理", "烹饪", "吃货", "美食制作"],
            "情感": ["情感", "心理", "人际关系", "情感咨询", "恋爱"]
        },
        "小红书": {
            "通用": ["#干货分享", "#经验分享", "#生活记录", "#学习", "#成长"],
            "科技": ["#科技好物", "#数码", "#AI工具", "#效率工具", "#科技生活"],
            "生活": ["#生活碎片", "#日常", "#生活方式", "#自律", "#极简生活"],
            "职场": ["#职场干货", "#打工人", "#职场日常", "#求职", "#面试"],
            "美食": ["#美食", "#美食日常", "#一人食", "#减脂餐", "#家常菜"],
            "情感": ["#情感", "#恋爱", "#crush", "#约会", "#情感树洞"]
        }
    }
    
    def __init__(self):
        """初始化标题优化器"""
        pass
    
    def generate_titles(self, topic: str, platform: str = "抖音", 
                       style: Optional[str] = None, count: int = 10,
                       pain_point: Optional[str] = None,
                       benefit: Optional[str] = None) -> Dict:
        """
        生成标题
        
        Args:
            topic: 话题
            platform: 平台
            style: 标题风格（可选）
            count: 生成数量
            pain_point: 痛点（可选）
            benefit: 收益（可选）
            
        Returns:
            标题结果字典
        """
        results = {
            "topic": topic,
            "platform": platform,
            "generated_count": count,
            "titles": []
        }
        
        # 确定要使用的风格
        styles = [style] if style else list(self.TITLE_FORMULAS.keys())
        
        # 每个风格平均分配数量
        titles_per_style = count // len(styles)
        extra = count % len(styles)
        
        for i, s in enumerate(styles):
            num = titles_per_style + (1 if i < extra else 0)
            style_titles = self._generate_style_titles(
                topic, platform, s, num, pain_point, benefit
            )
            results["titles"].extend(style_titles)
        
        return results
    
    def _generate_style_titles(self, topic: str, platform: str, style: str,
                               count: int, pain_point: Optional[str],
                               benefit: Optional[str]) -> List[Dict]:
        """生成特定风格的标题"""
        titles = []
        
        # 获取该风格的模板
        style_templates = self.TITLE_FORMULAS.get(style, {})
        platform_templates = style_templates.get(platform, style_templates.get("抖音", []))
        
        if not platform_templates:
            platform_templates = style_templates.get("抖音", ["{话题}干货分享"])
        
        # 随机选择模板并填充
        selected_templates = random.sample(platform_templates, min(count, len(platform_templates)))
        
        for template in selected_templates:
            title = template.format(
                话题=topic,
                痛点=pain_point or f"不会{topic}",
                收益=benefit or f"掌握{topic}",
                数字=random.choice([3, 5, 7, 10])
            )
            
            titles.append({
                "title": title,
                "style": style,
                "platform": platform,
                "score": self._calculate_title_score(title, platform)
            })
        
        return titles
    
    def _calculate_title_score(self, title: str, platform: str) -> int:
        """
        计算标题评分
        
        Args:
            title: 标题
            platform: 平台
            
        Returns:
            评分（0-100）
        """
        score = 70  # 基础分
        
        # 长度检查
        if platform == "抖音":
            if 15 <= len(title) <= 30:
                score += 10
        elif platform == "B站":
            if 20 <= len(title) <= 40:
                score += 10
        elif platform == "小红书":
            if 10 <= len(title) <= 25:
                score += 10
        
        # 包含数字加分
        if any(c.isdigit() for c in title):
            score += 10
        
        # 包含问号或感叹号加分
        if '？' in title or '!' in title or '！' in title:
            score += 5
        
        # 包含热门词汇加分
        hot_words = ['干货', '技巧', '方法', '教程', '必看', '收藏']
        if any(word in title for word in hot_words):
            score += 5
        
        return min(score, 100)
    
    def generate_tags(self, topic: str, platform: str, category: str = "通用", 
                     count: int = 5) -> List[str]:
        """
        生成标签
        
        Args:
            topic: 话题
            platform: 平台
            category: 内容分类
            count: 标签数量
            
        Returns:
            标签列表
        """
        platform_tags = self.PLATFORM_TAGS.get(platform, {})
        category_tags = platform_tags.get(category, platform_tags.get("通用", []))
        
        # 添加话题相关标签
        related_tags = [f"#{topic}", f"#{topic}分享", f"#{topic}干货"]
        
        all_tags = category_tags + related_tags
        
        # 去重并限制数量
        all_tags = list(dict.fromkeys(all_tags))
        
        if platform == "B站":
            # B站标签不需要#
            all_tags = [tag.replace('#', '') for tag in all_tags]
        
        return all_tags[:count]
    
    def analyze_title(self, title: str, platform: str) -> Dict:
        """
        分析标题质量
        
        Args:
            title: 标题
            platform: 平台
            
        Returns:
            分析结果
        """
        analysis = {
            "title": title,
            "platform": platform,
            "length": len(title),
            "score": self._calculate_title_score(title, platform),
            "suggestions": []
        }
        
        # 长度建议
        if platform == "抖音":
            if len(title) < 15:
                analysis["suggestions"].append("标题稍短，建议15-30字")
            elif len(title) > 30:
                analysis["suggestions"].append("标题较长，建议控制在30字以内")
        elif platform == "B站":
            if len(title) < 20:
                analysis["suggestions"].append("标题稍短，建议20-40字")
        
        # 数字建议
        if not any(c.isdigit() for c in title):
            analysis["suggestions"].append("建议加入数字，如'3个技巧'")
        
        # 标点建议
        if '？' not in title and '！' not in title and '?' not in title and '!' not in title:
            analysis["suggestions"].append("可适当加入问号或感叹号增加吸引力")
        
        return analysis
    
    def format_output_markdown(self, results: Dict) -> str:
        """
        格式化为Markdown输出
        
        Args:
            results: 结果字典
            
        Returns:
            Markdown字符串
        """
        md = f"""# 标题优化报告

## 📋 分析信息
- **话题**: {results['topic']}
- **平台**: {results['platform']}
- **生成数量**: {results['generated_count']}

---

## 📝 推荐标题

| 序号 | 标题 | 风格 | 评分 |
|------|------|------|------|
"""
        
        for i, title_info in enumerate(results['titles'], 1):
            md += f"| {i} | {title_info['title']} | {title_info['style']} | {title_info['score']} |\n"
        
        md += "\n---\n\n## 🏷️ 推荐标签\n"
        
        tags = self.generate_tags(results['topic'], results['platform'])
        for tag in tags:
            md += f"- {tag}\n"
        
        md += "\n---\n\n## 💡 优化建议\n"
        md += "1. 选择评分较高的标题\n"
        md += "2. 根据内容选择合适风格\n"
        md += "3. 标题要真实反映内容\n"
        md += "4. 避免标题党，保持诚信\n"
        
        return md


def main():
    """命令行入口"""
    parser = argparse.ArgumentParser(
        description='标题优化工具',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python title_optimizer.py --topic "时间管理" --platform 抖音 --count 10
  python title_optimizer.py --topic "AI工具" --platform B站 --style 数字型
  python title_optimizer.py --analyze "你的标题" --platform 抖音
        """
    )
    
    parser.add_argument(
        '--topic', '-t',
        help='视频话题/主题'
    )
    parser.add_argument(
        '--platform', '-p',
        choices=['抖音', 'B站', '小红书', '视频号'],
        default='抖音',
        help='目标平台（默认：抖音）'
    )
    parser.add_argument(
        '--style', '-s',
        choices=['悬念型', '数字型', '痛点型', '反常识型', '教程型'],
        help='标题风格（不指定则生成多种风格）'
    )
    parser.add_argument(
        '--count', '-c',
        type=int,
        default=10,
        help='生成标题数量（默认：10）'
    )
    parser.add_argument(
        '--pain-point',
        help='用户痛点（用于生成标题）'
    )
    parser.add_argument(
        '--benefit',
        help='用户收益（用于生成标题）'
    )
    parser.add_argument(
        '--analyze',
        help='分析指定标题的质量'
    )
    parser.add_argument(
        '--output', '-o',
        choices=['json', 'markdown', 'md'],
        default='markdown',
        help='输出格式（默认：markdown）'
    )
    
    args = parser.parse_args()
    
    optimizer = TitleOptimizer()
    
    # 分析模式
    if args.analyze:
        result = optimizer.analyze_title(args.analyze, args.platform)
        if args.output == 'json':
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            print(f"\n标题分析：{result['title']}")
            print(f"评分：{result['score']}/100")
            print(f"长度：{result['length']}字")
            print("\n优化建议：")
            for suggestion in result['suggestions']:
                print(f"- {suggestion}")
        return
    
    # 生成模式
    if not args.topic:
        parser.error('请指定话题（--topic）或使用 --analyze 分析标题')
    
    results = optimizer.generate_titles(
        topic=args.topic,
        platform=args.platform,
        style=args.style,
        count=args.count,
        pain_point=args.pain_point,
        benefit=args.benefit
    )
    
    if args.output == 'json':
        # 添加标签
        results['tags'] = optimizer.generate_tags(args.topic, args.platform)
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        print(optimizer.format_output_markdown(results))


if __name__ == '__main__':
    main()
