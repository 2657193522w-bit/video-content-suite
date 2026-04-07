#!/usr/bin/env python3
"""
视频脚本生成模块

功能：
- 生成完整的视频脚本（开头Hook + 正文 + CTA结尾）
- 支持多种平台格式（抖音、B站、小红书）
- 智能控制时长与节奏
- 提供拍摄建议

使用方法：
    python script_generator.py --topic "时间管理" --platform 抖音 --duration 30
    python script_generator.py --topic "AI工具" --platform B站 --duration 180 --style 知识分享
"""

import json
import argparse
from datetime import datetime
from typing import Dict, List, Optional


class ScriptGenerator:
    """视频脚本生成器"""
    
    # 平台配置
    PLATFORM_CONFIG = {
        "抖音": {
            "short_duration": (15, 60),
            "medium_duration": (60, 180),
            "style": ["快节奏", "强节奏", "视觉冲击"],
            "words_per_second": 4.5,
            "hook_templates": [
                "看完这个，我再也不{痛点}了",
                "99%的人都不知道{话题}的真相",
                "如果你也在{痛点}，一定要看完",
                "{数字}个技巧，让你{收益}",
                "原来{反常识观点}才是对的"
            ],
            "cta_templates": [
                "觉得有用的话，点个赞收藏吧",
                "关注我，每天分享{领域}干货",
                "评论区告诉我你的{问题}",
                "下期教你{预告内容}，记得关注"
            ]
        },
        "B站": {
            "short_duration": (180, 600),
            "medium_duration": (600, 1800),
            "style": ["深度解析", "知识分享", "轻松幽默"],
            "words_per_second": 3.5,
            "hook_templates": [
                "今天我们来聊聊{话题}",
                "关于{话题}，我发现了一个很有意思的现象",
                "大家好，这期视频我想和大家探讨{话题}",
                "{数字}分钟带你了解{话题}",
                "这可能是全网最详细的{话题}解析"
            ],
            "cta_templates": [
                "如果这期视频对你有帮助，别忘了三连支持",
                "欢迎在弹幕和评论区分享你的看法",
                "关注我的频道，获取更多{领域}内容",
                "下期视频预告：{预告内容}"
            ]
        },
        "小红书": {
            "short_duration": (30, 120),
            "medium_duration": (120, 300),
            "style": ["生活化", "真实分享", "种草属性"],
            "words_per_second": 4.0,
            "hook_templates": [
                "姐妹们，我发现了一个{话题}的宝藏方法",
                "{痛点}的姐妹看过来！",
                "亲测有效！{话题}攻略",
                "{数字}个{话题}小技巧，建议收藏",
                "后悔没早点知道{话题}"
            ],
            "cta_templates": [
                "觉得有用就点个赞吧，有问题评论区问我",
                "关注我，分享更多{领域}干货",
                "收藏起来慢慢看，下次找得到",
                "下期分享{预告内容}，记得来看"
            ]
        },
        "视频号": {
            "short_duration": (30, 120),
            "medium_duration": (120, 600),
            "style": ["正能量", "实用", "情感共鸣"],
            "words_per_second": 4.0,
            "hook_templates": [
                "今天想和大家分享{话题}",
                "关于{话题}，我有话要说",
                "{数字}年经验总结：{话题}",
                "如果你{痛点}，请认真看完",
                "{话题}，你做对了吗？"
            ],
            "cta_templates": [
                "喜欢的话点个赞，转发给需要的朋友",
                "关注我，一起成长",
                "评论区说说你的想法",
                "下期我们聊{预告内容}"
            ]
        }
    }
    
    def __init__(self):
        """初始化脚本生成器"""
        pass
    
    def calculate_word_count(self, duration: int, platform: str) -> int:
        """
        根据时长和平台计算建议字数
        
        Args:
            duration: 视频时长（秒）
            platform: 平台名称
            
        Returns:
            建议字数
        """
        wps = self.PLATFORM_CONFIG.get(platform, {}).get("words_per_second", 4.0)
        return int(duration * wps)
    
    def generate_hook(self, topic: str, platform: str, pain_point: Optional[str] = None) -> str:
        """
        生成开头Hook
        
        Args:
            topic: 话题
            platform: 平台
            pain_point: 痛点（可选）
            
        Returns:
            Hook文案
        """
        templates = self.PLATFORM_CONFIG.get(platform, {}).get("hook_templates", [])
        if not templates:
            return f"今天我们来聊聊{topic}"
        
        import random
        template = random.choice(templates)
        
        # 填充模板
        hook = template.format(
            topic=topic,
            痛点=pain_point or f"不会{topic}",
            收益=f"轻松掌握{topic}",
            数字=random.choice([3, 5, 7]),
            反常识观点=f"{topic}不是你想的那样",
            领域=topic[:2]
        )
        
        return hook
    
    def generate_body(self, topic: str, platform: str, duration: int, 
                     key_points: Optional[List[str]] = None) -> str:
        """
        生成正文内容
        
        Args:
            topic: 话题
            platform: 平台
            duration: 时长
            key_points: 关键要点（可选）
            
        Returns:
            正文文案
        """
        word_count = self.calculate_word_count(duration, platform)
        
        # 分配字数：Hook占10%，正文占75%，CTA占15%
        body_words = int(word_count * 0.75)
        
        if not key_points:
            # 生成默认要点
            key_points = [
                f"首先，我们要理解{topic}的核心概念",
                f"其次，{topic}在实际应用中有几个关键点",
                f"最后，我来分享一个实用的{topic}技巧"
            ]
        
        # 根据平台调整风格
        if platform == "抖音":
            body = self._generate_douyin_body(topic, key_points, body_words)
        elif platform == "B站":
            body = self._generate_bilibili_body(topic, key_points, body_words)
        elif platform == "小红书":
            body = self._generate_xiaohongshu_body(topic, key_points, body_words)
        else:
            body = self._generate_default_body(topic, key_points, body_words)
        
        return body
    
    def _generate_douyin_body(self, topic: str, key_points: List[str], word_count: int) -> str:
        """生成抖音风格正文"""
        body_parts = []
        for i, point in enumerate(key_points, 1):
            if i == 1:
                body_parts.append(f"第一，{point}。很多人不知道，其实{topic}很简单。")
            elif i == 2:
                body_parts.append(f"第二，{point}。记住这一点，你就超过了90%的人。")
            else:
                body_parts.append(f"第三，{point}。这个技巧特别实用。")
        
        body = " ".join(body_parts)
        
        # 控制字数
        if len(body) > word_count:
            body = body[:word_count] + "..."
        
        return body
    
    def _generate_bilibili_body(self, topic: str, key_points: List[str], word_count: int) -> str:
        """生成B站风格正文"""
        body_parts = [f"首先，我们需要了解{topic}的基本概念。"]
        
        for point in key_points:
            body_parts.append(f"{point}。这里我要特别强调一下，很多人容易忽略这个细节。")
        
        body_parts.append(f"总结一下，{topic}的关键在于理解和实践。希望这期内容对你有帮助。")
        
        body = " ".join(body_parts)
        return body[:word_count] if len(body) > word_count else body
    
    def _generate_xiaohongshu_body(self, topic: str, key_points: List[str], word_count: int) -> str:
        """生成小红书风格正文"""
        body_parts = [f"亲测分享！关于{topic}，我总结了几点经验："]
        
        for i, point in enumerate(key_points, 1):
            body_parts.append(f"✨ {point}")
        
        body_parts.append(f"这些都是我自己实践过的，真的很有用！")
        
        body = "\n".join(body_parts)
        return body[:word_count] if len(body) > word_count else body
    
    def _generate_default_body(self, topic: str, key_points: List[str], word_count: int) -> str:
        """生成默认风格正文"""
        body_parts = []
        for point in key_points:
            body_parts.append(point + "。")
        
        body = " ".join(body_parts)
        return body[:word_count] if len(body) > word_count else body
    
    def generate_cta(self, topic: str, platform: str, next_topic: Optional[str] = None) -> str:
        """
        生成结尾CTA
        
        Args:
            topic: 话题
            platform: 平台
            next_topic: 下期预告话题（可选）
            
        Returns:
            CTA文案
        """
        templates = self.PLATFORM_CONFIG.get(platform, {}).get("cta_templates", [])
        if not templates:
            return "记得点赞关注！"
        
        import random
        template = random.choice(templates)
        
        cta = template.format(
            领域=topic[:2],
            问题=f"关于{topic}的问题",
            预告内容=next_topic or f"更多{topic}技巧"
        )
        
        return cta
    
    def generate_script(self, topic: str, platform: str = "抖音", 
                       duration: int = 60, style: Optional[str] = None,
                       key_points: Optional[List[str]] = None,
                       pain_point: Optional[str] = None,
                       next_topic: Optional[str] = None) -> Dict:
        """
        生成完整脚本
        
        Args:
            topic: 话题主题
            platform: 目标平台
            duration: 视频时长（秒）
            style: 内容风格（可选）
            key_points: 关键要点（可选）
            pain_point: 痛点（可选）
            next_topic: 下期预告（可选）
            
        Returns:
            完整脚本字典
        """
        script = {
            "metadata": {
                "topic": topic,
                "platform": platform,
                "duration": duration,
                "style": style or "默认",
                "created_at": datetime.now().isoformat(),
                "word_count": self.calculate_word_count(duration, platform)
            },
            "hook": self.generate_hook(topic, platform, pain_point),
            "body": self.generate_body(topic, platform, duration, key_points),
            "cta": self.generate_cta(topic, platform, next_topic),
            "suggestions": {
                "shooting_tips": self._get_shooting_tips(platform),
                "editing_tips": self._get_editing_tips(platform),
                "best_time": self._get_best_time(platform)
            }
        }
        
        return script
    
    def _get_shooting_tips(self, platform: str) -> List[str]:
        """获取拍摄建议"""
        tips = {
            "抖音": [
                "使用竖屏9:16比例",
                "保持画面稳定，可用手机云台",
                "光线充足，面部清晰可见",
                "背景简洁，避免杂乱"
            ],
            "B站": [
                "横屏16:9比例",
                "音质清晰，建议使用麦克风",
                "画面要有变化，避免一镜到底",
                "适当添加字幕和标注"
            ],
            "小红书": [
                "竖屏9:16比例",
                "画面要美，注重颜值",
                "光线柔和自然",
                "可适当使用滤镜"
            ],
            "视频号": [
                "竖屏9:16为主",
                "内容真实自然",
                "声音清晰洪亮",
                "背景与主题相关"
            ]
        }
        return tips.get(platform, tips["抖音"])
    
    def _get_editing_tips(self, platform: str) -> List[str]:
        """获取剪辑建议"""
        tips = {
            "抖音": [
                "开头3秒必须抓人",
                "节奏要快，删减停顿",
                "添加热门BGM",
                "使用平台热门特效"
            ],
            "B站": [
                "添加片头片尾",
                "关键信息加字幕",
                "适当添加表情包",
                "进度条提示"
            ],
            "小红书": [
                "封面要精美",
                "添加花字和贴纸",
                "使用平台热门音乐",
                "色调统一"
            ],
            "视频号": [
                "内容真实不做作",
                "字幕清晰可读",
                "音乐与内容匹配",
                "时长控制在合适范围"
            ]
        }
        return tips.get(platform, tips["抖音"])
    
    def _get_best_time(self, platform: str) -> str:
        """获取最佳发布时间"""
        times = {
            "抖音": "7-9点、12-14点、18-22点",
            "B站": "11-13点、17-19点、21-23点",
            "小红书": "7-9点、12-13点、18-22点",
            "视频号": "7-9点、12-14点、20-22点"
        }
        return times.get(platform, "18-22点")
    
    def format_script_markdown(self, script: Dict) -> str:
        """
        将脚本格式化为Markdown
        
        Args:
            script: 脚本字典
            
        Returns:
            Markdown格式字符串
        """
        meta = script["metadata"]
        
        md = f"""# 视频脚本：{meta['topic']}

## 📋 基础信息
- **话题**: {meta['topic']}
- **平台**: {meta['platform']}
- **时长**: {meta['duration']}秒
- **建议字数**: {meta['word_count']}字
- **风格**: {meta['style']}

---

## 🎣 开头Hook（0-3秒）
{script['hook']}

---

## 📝 正文内容
{script['body']}

---

## 🎯 结尾CTA
{script['cta']}

---

## 📸 拍摄建议
"""
        for tip in script['suggestions']['shooting_tips']:
            md += f"- {tip}\n"
        
        md += "\n## ✂️ 剪辑建议\n"
        for tip in script['suggestions']['editing_tips']:
            md += f"- {tip}\n"
        
        md += f"\n## ⏰ 最佳发布时间\n{script['suggestions']['best_time']}\n"
        
        return md


def main():
    """命令行入口"""
    parser = argparse.ArgumentParser(
        description='视频脚本生成工具',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python script_generator.py --topic "时间管理" --platform 抖音 --duration 30
  python script_generator.py --topic "AI工具" --platform B站 --duration 180
  python script_generator.py --topic "健身入门" --platform 小红书 --duration 60 --output json
        """
    )
    
    parser.add_argument(
        '--topic', '-t',
        required=True,
        help='视频话题/主题'
    )
    parser.add_argument(
        '--platform', '-p',
        choices=['抖音', 'B站', '小红书', '视频号'],
        default='抖音',
        help='目标平台（默认：抖音）'
    )
    parser.add_argument(
        '--duration', '-d',
        type=int,
        default=60,
        help='视频时长（秒，默认：60）'
    )
    parser.add_argument(
        '--style', '-s',
        help='内容风格（如：知识分享、娱乐搞笑）'
    )
    parser.add_argument(
        '--output', '-o',
        choices=['json', 'markdown', 'md'],
        default='markdown',
        help='输出格式（默认：markdown）'
    )
    parser.add_argument(
        '--pain-point',
        help='用户痛点（用于生成Hook）'
    )
    parser.add_argument(
        '--next-topic',
        help='下期预告话题'
    )
    
    args = parser.parse_args()
    
    # 初始化生成器
    generator = ScriptGenerator()
    
    # 生成脚本
    script = generator.generate_script(
        topic=args.topic,
        platform=args.platform,
        duration=args.duration,
        style=args.style,
        pain_point=args.pain_point,
        next_topic=args.next_topic
    )
    
    # 输出结果
    if args.output == 'json':
        print(json.dumps(script, ensure_ascii=False, indent=2))
    else:
        print(generator.format_script_markdown(script))


if __name__ == '__main__':
    main()

