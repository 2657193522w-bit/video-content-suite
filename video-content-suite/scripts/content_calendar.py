#!/usr/bin/env python3
"""
内容日历模块

功能：
- 生成内容发布计划
- 推荐每日话题
- 标注最佳发布时间
- 支持多种发布频率

使用方法：
    python content_calendar.py --start 2026-04-08 --days 7 --frequency daily
    python content_calendar.py --start 2026-04-08 --days 30 --platform 抖音 --category 科技
"""

import json
import argparse
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import random


class ContentCalendar:
    """内容日历生成器"""
    
    # 话题库
    TOPIC_LIBRARY = {
        "科技": [
            "AI工具推荐", "ChatGPT使用技巧", "效率软件分享", "数码产品测评",
            "科技资讯解读", "编程学习", "科技好物", "AI绘画教程",
            "自动化工具", "科技趋势分析", "智能家居", "科技冷知识"
        ],
        "生活": [
            "晨间routine", "极简生活", "自律养成", "阅读习惯",
            "健身打卡", "生活方式", "独居生活", "低成本爱好",
            "生活小技巧", "收纳整理", "断舍离", "生活vlog"
        ],
        "职场": [
            "面试技巧", "职场沟通", "升职加薪", "副业推荐",
            "时间管理", "工作效率", "职业规划", "简历优化",
            "职场礼仪", "远程办公", "团队协作", "职场避坑"
        ],
        "美食": [
            "快手菜教程", "减脂餐分享", "空气炸锅美食", "一人食",
            "家常菜做法", "烘焙入门", "美食探店", "预制菜测评",
            "省钱食谱", "美食vlog", "饮品制作", "美食摄影"
        ],
        "情感": [
            "恋爱技巧", "约会指南", "情感共鸣", "人际关系",
            "社交技巧", "边界感", "自我成长", "情感树洞",
            "crush攻略", "分手疗愈", "单身生活", "情感咨询"
        ],
        "学习": [
            "学习方法", "考试技巧", "知识分享", "读书笔记",
            "语言学习", "技能提升", "在线课程", "学习vlog",
            "知识科普", "思维模型", "记忆技巧", "专注力训练"
        ]
    }
    
    # 平台最佳发布时间
    PLATFORM_SCHEDULE = {
        "抖音": {
            "weekday": ["7:00-9:00", "12:00-14:00", "18:00-22:00"],
            "weekend": ["9:00-11:00", "14:00-16:00", "19:00-23:00"]
        },
        "B站": {
            "weekday": ["11:00-13:00", "17:00-19:00", "21:00-23:00"],
            "weekend": ["10:00-12:00", "15:00-17:00", "20:00-24:00"]
        },
        "小红书": {
            "weekday": ["7:00-9:00", "12:00-13:00", "18:00-22:00"],
            "weekend": ["9:00-11:00", "13:00-15:00", "19:00-23:00"]
        },
        "视频号": {
            "weekday": ["7:00-9:00", "12:00-14:00", "20:00-22:00"],
            "weekend": ["9:00-11:00", "14:00-16:00", "20:00-22:00"]
        }
    }
    
    # 内容类型
    CONTENT_TYPES = {
        "抖音": ["教程", "测评", "vlog", "挑战", "干货"],
        "B站": ["深度解析", "教程", "vlog", "测评", "知识分享"],
        "小红书": ["种草", "教程", "测评", "plog", "干货"],
        "视频号": ["正能量", "教程", "生活", "干货", "情感"]
    }
    
    def __init__(self):
        """初始化内容日历生成器"""
        pass
    
    def generate_calendar(self, start_date: str, days: int = 7,
                         platform: str = "抖音", category: str = "生活",
                         frequency: str = "daily") -> Dict:
        """
        生成内容日历
        
        Args:
            start_date: 开始日期（YYYY-MM-DD格式）
            days: 天数
            platform: 目标平台
            category: 内容分类
            frequency: 发布频率（daily/weekly/custom）
            
        Returns:
            日历字典
        """
        calendar = {
            "metadata": {
                "start_date": start_date,
                "days": days,
                "platform": platform,
                "category": category,
                "frequency": frequency,
                "created_at": datetime.now().isoformat()
            },
            "schedule": []
        }
        
        # 解析开始日期
        start = datetime.strptime(start_date, "%Y-%m-%d")
        
        # 获取话题库
        topics = self.TOPIC_LIBRARY.get(category, self.TOPIC_LIBRARY["生活"])
        
        # 生成每日计划
        for i in range(days):
            current_date = start + timedelta(days=i)
            date_str = current_date.strftime("%Y-%m-%d")
            is_weekend = current_date.weekday() >= 5
            
            # 根据频率确定是否发布
            if frequency == "daily":
                should_post = True
            elif frequency == "weekly":
                should_post = current_date.weekday() == 0  # 每周一
            elif frequency == "custom":
                should_post = current_date.weekday() in [0, 3]  # 周一、周四
            else:
                should_post = True
            
            if should_post:
                # 随机选择话题
                topic = random.choice(topics)
                content_type = random.choice(self.CONTENT_TYPES.get(platform, ["干货"]))
                
                # 获取发布时间
                best_times = self._get_best_times(platform, is_weekend)
                
                day_plan = {
                    "date": date_str,
                    "weekday": current_date.strftime("%A"),
                    "is_weekend": is_weekend,
                    "topic": topic,
                    "content_type": content_type,
                    "best_times": best_times,
                    "status": "planned",
                    "notes": ""
                }
                
                calendar["schedule"].append(day_plan)
        
        return calendar
    
    def _get_best_times(self, platform: str, is_weekend: bool) -> List[str]:
        """
        获取最佳发布时间
        
        Args:
            platform: 平台
            is_weekend: 是否周末
            
        Returns:
            时间列表
        """
        schedule = self.PLATFORM_SCHEDULE.get(platform, self.PLATFORM_SCHEDULE["抖音"])
        key = "weekend" if is_weekend else "weekday"
        return schedule.get(key, ["18:00-22:00"])
    
    def add_content_ideas(self, calendar: Dict, count: int = 3) -> Dict:
        """
        为每个计划添加内容创意
        
        Args:
            calendar: 日历字典
            count: 每个计划的创意数量
            
        Returns:
            更新后的日历
        """
        for day in calendar["schedule"]:
            topic = day["topic"]
            content_type = day["content_type"]
            
            ideas = self._generate_content_ideas(topic, content_type, count)
            day["content_ideas"] = ideas
        
        return calendar
    
    def _generate_content_ideas(self, topic: str, content_type: str, count: int) -> List[str]:
        """生成内容创意"""
        idea_templates = {
            "教程": [
                f"手把手教你{topic}的3个技巧",
                f"{topic}入门到精通，一个视频讲清楚",
                f"新手必看：{topic}避坑指南"
            ],
            "测评": [
                f"{topic}产品实测，哪款最值得买",
                f"亲测{topic}，结果出乎意料",
                f"{topic}横向对比，帮你省钱"
            ],
            "vlog": [
                f"我的{topic}日常，真实记录",
                f"{topic}的一天，原来是这样的",
                f"沉浸式体验{topic}"
            ],
            "干货": [
                f"关于{topic}，没人告诉你的真相",
                f"{topic}的5个核心要点",
                f"{topic}经验总结，建议收藏"
            ],
            "种草": [
                f"这个{topic}神器，太好用了",
                f"{topic}好物分享，亲测有效",
                f"后悔没早点发现这个{topic}"
            ],
            "深度解析": [
                f"{topic}深度解析：底层逻辑",
                f"关于{topic}，你可能理解错了",
                f"{topic}的本质，一个视频讲透"
            ]
        }
        
        templates = idea_templates.get(content_type, idea_templates["干货"])
        return random.sample(templates, min(count, len(templates)))
    
    def export_to_markdown(self, calendar: Dict) -> str:
        """
        导出为Markdown格式
        
        Args:
            calendar: 日历字典
            
        Returns:
            Markdown字符串
        """
        meta = calendar["metadata"]
        
        md = f"""# 内容发布日历

## 📋 计划概览
- **开始日期**: {meta['start_date']}
- **计划天数**: {meta['days']}天
- **目标平台**: {meta['platform']}
- **内容分类**: {meta['category']}
- **发布频率**: {meta['frequency']}

---

## 📅 发布计划

| 日期 | 星期 | 话题 | 类型 | 最佳时间 | 状态 |
|------|------|------|------|----------|------|
"""
        
        for day in calendar["schedule"]:
            times = " / ".join(day["best_times"])
            md += f"| {day['date']} | {day['weekday']} | {day['topic']} | {day['content_type']} | {times} | {day['status']} |\n"
        
        md += "\n---\n\n## 💡 内容创意详情\n\n"
        
        for day in calendar["schedule"]:
            md += f"### {day['date']} ({day['weekday']}) - {day['topic']}\n\n"
            md += f"- **内容类型**: {day['content_type']}\n"
            md += f"- **最佳发布时间**: {', '.join(day['best_times'])}\n"
            
            if "content_ideas" in day:
                md += "- **创意方向**:\n"
                for idea in day["content_ideas"]:
                    md += f"  - {idea}\n"
            
            if day["notes"]:
                md += f"- **备注**: {day['notes']}\n"
            
            md += "\n"
        
        md += """---

## 📝 使用建议

1. **提前准备**: 建议提前1-2天准备好内容
2. **灵活调整**: 根据实际情况调整发布时间和话题
3. **数据追踪**: 记录每条内容的数据表现，优化后续计划
4. **热点结合**: 关注实时热点，及时调整内容方向
5. **互动维护**: 发布后及时回复评论，增加互动

## 🎯 优化建议

- 根据历史数据调整最佳发布时间
- 分析爆款内容，总结成功经验
- 保持内容风格的统一性
- 定期回顾和优化内容策略
"""
        
        return md
    
    def export_to_json(self, calendar: Dict) -> str:
        """
        导出为JSON格式
        
        Args:
            calendar: 日历字典
            
        Returns:
            JSON字符串
        """
        return json.dumps(calendar, ensure_ascii=False, indent=2)


def main():
    """命令行入口"""
    parser = argparse.ArgumentParser(
        description='内容日历生成工具',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python content_calendar.py --start 2026-04-08 --days 7
  python content_calendar.py --start 2026-04-08 --days 30 --platform B站 --category 科技
  python content_calendar.py --start 2026-04-08 --days 14 --frequency weekly --output json
        """
    )
    
    parser.add_argument(
        '--start', '-s',
        required=True,
        help='开始日期（格式：YYYY-MM-DD）'
    )
    parser.add_argument(
        '--days', '-d',
        type=int,
        default=7,
        help='计划天数（默认：7）'
    )
    parser.add_argument(
        '--platform', '-p',
        choices=['抖音', 'B站', '小红书', '视频号'],
        default='抖音',
        help='目标平台（默认：抖音）'
    )
    parser.add_argument(
        '--category', '-c',
        choices=['科技', '生活', '职场', '美食', '情感', '学习'],
        default='生活',
        help='内容分类（默认：生活）'
    )
    parser.add_argument(
        '--frequency', '-f',
        choices=['daily', 'weekly', 'custom'],
        default='daily',
        help='发布频率（daily=每天, weekly=每周, custom=自定义）'
    )
    parser.add_argument(
        '--ideas',
        type=int,
        default=3,
        help='每个计划的内容创意数量（默认：3）'
    )
    parser.add_argument(
        '--output', '-o',
        choices=['json', 'markdown', 'md'],
        default='markdown',
        help='输出格式（默认：markdown）'
    )
    
    args = parser.parse_args()
    
    # 验证日期格式
    try:
        datetime.strptime(args.start, "%Y-%m-%d")
    except ValueError:
        parser.error('日期格式错误，请使用 YYYY-MM-DD 格式')
    
    # 初始化生成器
    generator = ContentCalendar()
    
    # 生成日历
    calendar = generator.generate_calendar(
        start_date=args.start,
        days=args.days,
        platform=args.platform,
        category=args.category,
        frequency=args.frequency
    )
    
    # 添加内容创意
    if args.ideas > 0:
        calendar = generator.add_content_ideas(calendar, args.ideas)
    
    # 输出结果
    if args.output == 'json':
        print(generator.export_to_json(calendar))
    else:
        print(generator.export_to_markdown(calendar))


if __name__ == '__main__':
    main()
