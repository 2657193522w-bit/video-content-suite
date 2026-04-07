# Video Content Suite 🎬

AI视频内容创作套件 - 帮助内容创作者自动化生成视频脚本、优化口播文案、生成SEO友好的标题标签，以及规划内容发布日历。

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## ✨ 功能特性

### 📝 视频脚本生成
- 智能生成完整脚本（Hook + 正文 + CTA）
- 支持抖音、B站、小红书、视频号等平台差异化风格
- 自动计算建议字数和时长
- 提供拍摄和剪辑建议

### 🔥 热点趋势分析
- 多领域热点话题库（科技、生活、职场、美食、情感等）
- 平台趋势洞察
- 选题建议生成
- 关键词分析

### 🏷️ 标题优化
- 5种标题风格（悬念型、数字型、痛点型、反常识型、教程型）
- 平台算法友好的标题生成
- SEO标签推荐
- 标题质量评分

### 📅 内容日历规划
- 自动生成发布计划
- 推荐每日话题和内容类型
- 标注最佳发布时间
- 支持多种发布频率

## 🚀 快速开始

### 安装

```bash
# 克隆仓库
git clone https://github.com/yourusername/video-content-suite.git
cd video-content-suite

# 安装依赖（Python 3.9+）
pip install -r requirements.txt
```

### 使用示例

#### 1. 生成视频脚本

```bash
python scripts/script_generator.py --topic "时间管理" --platform 抖音 --duration 30
```

输出示例：
```markdown
# 视频脚本：时间管理

## 📋 基础信息
- **话题**: 时间管理
- **平台**: 抖音
- **时长**: 30秒
- **建议字数**: 135字

## 🎣 开头Hook（0-3秒）
看完这个，我再也不拖延了

## 📝 正文内容
第一，用番茄工作法。25分钟专注，5分钟休息，效率翻倍。
第二，列每日清单。把大目标拆解成小任务，完成一项划一项。
第三，远离手机干扰。工作时手机放另一个房间。

## 🎯 结尾CTA
觉得有用的话，点个赞收藏吧！关注我，每天分享效率干货！
```

#### 2. 热点趋势分析

```bash
python scripts/trend_analyzer.py --category 科技 --platform 抖音
```

#### 3. 生成标题

```bash
python scripts/title_optimizer.py --topic "AI工具" --platform B站 --count 10
```

#### 4. 创建内容日历

```bash
python scripts/content_calendar.py --start 2026-04-08 --days 7 --platform 抖音 --category 职场
```

## 📚 详细文档

### 脚本生成器

```bash
python scripts/script_generator.py --help
```

参数说明：
- `--topic, -t`: 视频话题（必填）
- `--platform, -p`: 目标平台（默认：抖音）
- `--duration, -d`: 视频时长秒数（默认：60）
- `--style, -s`: 内容风格
- `--pain-point`: 用户痛点
- `--output, -o`: 输出格式（json/markdown）

### 热点分析器

```bash
python scripts/trend_analyzer.py --help
```

参数说明：
- `--category, -c`: 内容分类
- `--platform, -p`: 目标平台
- `--output, -o`: 输出格式
- `--list-categories`: 列出所有分类

### 标题优化器

```bash
python scripts/title_optimizer.py --help
```

参数说明：
- `--topic, -t`: 视频话题
- `--platform, -p`: 目标平台
- `--style, -s`: 标题风格
- `--count, -c`: 生成数量
- `--analyze`: 分析指定标题

### 内容日历

```bash
python scripts/content_calendar.py --help
```

参数说明：
- `--start, -s`: 开始日期（YYYY-MM-DD）
- `--days, -d`: 计划天数
- `--platform, -p`: 目标平台
- `--category, -c`: 内容分类
- `--frequency, -f`: 发布频率

## 📁 项目结构

```
video-content-suite/
├── SKILL.md                 # OpenClaw Skill定义文件
├── README.md                # 项目说明
├── LICENSE                  # MIT许可证
├── scripts/                 # Python脚本
│   ├── __init__.py
│   ├── trend_analyzer.py    # 热点分析
│   ├── script_generator.py  # 脚本生成
│   ├── title_optimizer.py   # 标题优化
│   └── content_calendar.py  # 内容日历
├── templates/               # 输出模板
│   ├── script-template.md
│   ├── title-formulas.json
│   └── calendar-template.md
├── config/                  # 配置文件
│   ├── platforms.json       # 平台规则
│   └── hot_topics.json      # 热点话题库
└── examples/                # 示例输出
    ├── example-script.md
    └── example-calendar.md
```

## 🎯 平台支持

| 平台 | 脚本生成 | 标题优化 | 热点分析 | 内容日历 |
|------|----------|----------|----------|----------|
| 抖音 | ✅ | ✅ | ✅ | ✅ |
| B站 | ✅ | ✅ | ✅ | ✅ |
| 小红书 | ✅ | ✅ | ✅ | ✅ |
| 视频号 | ✅ | ✅ | ✅ | ✅ |

## 🔧 配置说明

### 平台配置 (`config/platforms.json`)

包含各平台的内容规范：
- 视频时长限制
- 画面比例
- 标签数量
- 最佳发布时间
- 算法因素

### 热点话题库 (`config/hot_topics.json`)

可自定义的热点话题：
- 分类关键词
- trending话题
- 选题建议
- 痛点分析

## 🛠️ 开发计划

- [ ] Web界面
- [ ] API接口
- [ ] 更多平台支持
- [ ] AI模型集成
- [ ] 数据分析功能
- [ ] 团队协作功能

## 🤝 贡献指南

欢迎提交Issue和Pull Request！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开 Pull Request

## 📝 更新日志

### v1.0.0 (2026-04-07)
- 🎉 初始版本发布
- ✅ 脚本生成功能
- ✅ 热点分析功能
- ✅ 标题优化功能
- ✅ 内容日历功能
- ✅ 支持4大主流平台

## 📄 License

本项目采用 [MIT](LICENSE) 许可证开源。

## 🙏 致谢

感谢所有贡献者和用户的支持！

---

<p align="center">Made with ❤️ by OpenClaw Community</p>
