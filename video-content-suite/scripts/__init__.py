"""
Video Content Suite - AI视频内容创作套件

这是一个帮助内容创作者自动化视频内容创作的Python包。
包含热点分析、脚本生成、标题优化、内容日历等功能。

Modules:
    trend_analyzer: 热点趋势分析
    script_generator: 视频脚本生成
    title_optimizer: 标题与标签优化
    content_calendar: 内容发布日历规划

Author: OpenClaw Community
Version: 1.0.0
License: MIT
"""

__version__ = "1.0.0"
__author__ = "OpenClaw Community"

from .trend_analyzer import TrendAnalyzer
from .script_generator import ScriptGenerator
from .title_optimizer import TitleOptimizer
from .content_calendar import ContentCalendar

__all__ = [
    "TrendAnalyzer",
    "ScriptGenerator",
    "TitleOptimizer",
    "ContentCalendar",
]
