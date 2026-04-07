#!/usr/bin/env python3
"""
热点趋势分析模块

功能：
- 分析当前热点话题
- 提供选题建议
- 识别趋势关键词
- 推荐内容方向

使用方法：
    python trend_analyzer.py --category 科技 --platform 抖音
    python trend_analyzer.py --category 生活 --output json
"""

import json
import argparse
from datetime import datetime
from typing import List, Dict, Optional


class TrendAnalyzer:
    """热点趋势分析器"""
    
    def __init__(self, config_path: str = "../config/hot_topics.json"):
        """
        初始化分析器
        
        Args:
            config_path: 热点话题配置文件路径
        """
        self.config_path = config_path
        self.hot_topics = self._load_hot_topics()
        
    def _load_hot_topics(self) -> Dict:
        """加载热点话题库"""
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            # 返回默认热点话题
            return self._get_default_topics()
    
    def _get_default_topics(self) -> Dict:
        """获取默认热点话题库"""
        return {
            "categories": {
                "科技": {
                    "keywords": ["AI", "人工智能", "ChatGPT", "大模型", "科技测评"],
                    "trending": ["AI工具推荐", "ChatGPT使用技巧", "AI绘画教程"],
                    "suggestions": [
                        "AI工具实测对比",
                        "普通人如何用AI提升效率",
                        "AI时代必备技能"
                    ]
                },
                "生活": {
                    "keywords": ["自律", "早起", "阅读", "健身", "极简生活"],
                    "trending": ["晨间routine", "独居生活", "低成本爱好"],
                    "suggestions": [
                        "自律一年的变化",
                        "极简生活如何省钱",
                        "普通人如何开始健身"
                    ]
                },
                "职场": {
                    "keywords": ["升职加薪", "面试技巧", "副业", "远程办公"],
                    "trending": ["副业推荐", "面试避坑", "职场沟通"],
                    "suggestions": [
                        "面试必问的10个问题",
                        "副业收入超过主业",
                        "如何与领导高效沟通"
                    ]
                },
                "美食": {
                    "keywords": ["家常菜", "快手菜", "减脂餐", "烘焙"],
                    "trending": ["空气炸锅美食", "一人食", "预制菜测评"],
                    "suggestions": [
                        "10分钟快手晚餐",
                        "空气炸锅万能公式",
                        "减脂期也能吃的美食"
                    ]
                },
                "情感": {
                    "keywords": ["恋爱", "婚姻", "社交", "人际关系"],
                    "trending": ["crush", "约会技巧", "边界感"],
                    "suggestions": [
                        "如何识别对的人",
                        "健康的恋爱关系",
                        "社交恐惧症自救指南"
                    ]
                }
            },
            "platform_trends": {
                "抖音": {
                    "hot_formats": ["挑战", "教程", "测评", "vlog"],
                    "peak_hours": ["7-9", "12-14", "18-22"]
                },
                "B站": {
                    "hot_formats": ["深度解析", "知识分享", "开箱", "vlog"],
                    "peak_hours": ["11-13", "17-19", "21-23"]
                },
                "小红书": {
                    "hot_formats": ["种草", "教程", "测评", "plog"],
                    "peak_hours": ["7-9", "12-13", "18-22"]
                }
            }
        }
    
    def analyze_category(self, category: str, platform: Optional[str] = None) -> Dict:
        """
        分析指定领域的热点
        
        Args:
            category: 内容领域/分类
            platform: 目标平台（可选）
            
        Returns:
            分析结果字典
        """
        result = {
            "category": category,
            "analysis_time": datetime.now().isoformat(),
            "keywords": [],
            "trending_topics": [],
            "content_suggestions": [],
            "platform_insights": {}
        }
        
        # 获取分类数据
        cat_data = self.hot_topics.get("categories", {}).get(category, {})
        
        if cat_data:
            result["keywords"] = cat_data.get("keywords", [])
            result["trending_topics"] = cat_data.get("trending", [])
            result["content_suggestions"] = cat_data.get("suggestions", [])
        
        # 添加平台洞察
        if platform:
            platform_data = self.hot_topics.get("platform_trends", {}).get(platform, {})
            result["platform_insights"] = {
                "platform": platform,
                "hot_formats": platform_data.get("hot_formats", []),
                "peak_hours": platform_data.get("peak_hours", [])
            }
        
        return result
    
    def get_all_categories(self) -> List[str]:
        """获取所有可用的内容分类"""
        return list(self.hot_topics.get("categories", {}).keys())
    
    def suggest_topics(self, keywords: List[str], count: int = 5) -> List[str]:
        """
        基于关键词推荐话题
        
        Args:
            keywords: 关键词列表
            count: 推荐数量
            
        Returns:
            推荐话题列表
        """
        suggestions = []
        
        for category, data in self.hot_topics.get("categories", {}).items():
            cat_keywords = data.get("keywords", [])
            # 检查关键词匹配
            if any(kw in cat_keywords for kw in keywords):
                suggestions.extend(data.get("suggestions", []))
        
        # 去重并限制数量
        suggestions = list(dict.fromkeys(suggestions))
        return suggestions[:count]
    
    def generate_report(self, category: str, platform: Optional[str] = None) -> str:
        """
        生成热点分析报告
        
        Args:
            category: 内容领域
            platform: 目标平台
            
        Returns:
            Markdown格式的报告
        """
        analysis = self.analyze_category(category, platform)
        
        report = f"""# 热点趋势分析报告

## 分析概览
- **分析领域**: {analysis['category']}
- **分析时间**: {analysis['analysis_time']}
- **目标平台**: {platform or '全平台'}

## 🔥 热门关键词
"""
        
        for keyword in analysis['keywords']:
            report += f"- {keyword}\n"
        
        report += "\n## 📈  trending话题\n"
        for topic in analysis['trending_topics']:
            report += f"- {topic}\n"
        
        report += "\n## 💡 内容选题建议\n"
        for i, suggestion in enumerate(analysis['content_suggestions'], 1):
            report += f"{i}. {suggestion}\n"
        
        if analysis.get('platform_insights'):
            insights = analysis['platform_insights']
            report += f"\n## 📱 {platform}平台洞察\n"
            report += f"\n### 热门内容形式\n"
            for fmt in insights.get('hot_formats', []):
                report += f"- {fmt}\n"
            report += f"\n### 最佳发布时段\n"
            for hour in insights.get('peak_hours', []):
                report += f"- {hour}点\n"
        
        return report


def main():
    """命令行入口"""
    parser = argparse.ArgumentParser(
        description='热点趋势分析工具',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python trend_analyzer.py --category 科技
  python trend_analyzer.py --category 职场 --platform 抖音 --output json
  python trend_analyzer.py --list-categories
        """
    )
    
    parser.add_argument(
        '--category', '-c',
        help='内容领域/分类（如：科技、生活、职场）'
    )
    parser.add_argument(
        '--platform', '-p',
        choices=['抖音', 'B站', '小红书', '视频号'],
        help='目标平台'
    )
    parser.add_argument(
        '--output', '-o',
        choices=['json', 'markdown', 'md'],
        default='markdown',
        help='输出格式（默认：markdown）'
    )
    parser.add_argument(
        '--list-categories', '-l',
        action='store_true',
        help='列出所有可用的内容分类'
    )
    
    args = parser.parse_args()
    
    # 初始化分析器
    analyzer = TrendAnalyzer()
    
    # 列出分类
    if args.list_categories:
        categories = analyzer.get_all_categories()
        print("可用的内容分类：")
        for cat in categories:
            print(f"  - {cat}")
        return
    
    # 检查必要参数
    if not args.category:
        parser.error('请指定内容分类（--category）或使用 --list-categories 查看可用分类')
    
    # 执行分析
    if args.output == 'json':
        result = analyzer.analyze_category(args.category, args.platform)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        report = analyzer.generate_report(args.category, args.platform)
        print(report)


if __name__ == '__main__':
    main()
