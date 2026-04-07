# 浏览器操作准则

## 双节点浏览器架构

| 节点 | 模式 | 配置文件 | 用途 |
|------|------|----------|------|
| **Linux 网关** | 托管模式 | `openclaw` | 本地浏览器自动化 |
| **Mac 节点** | 扩展中继 | `mac` | 远程浏览器自动化 |

## 使用方式

### Linux 网关本地浏览器（托管模式）
```javascript
// 启动浏览器
browser({ action: "start", target: "host", profile: "openclaw" })

// 打开网页
browser({ action: "open", target: "host", profile: "openclaw", url: "https://..." })

// 截图
browser({ action: "screenshot", target: "host", profile: "openclaw" })
```

### Mac 节点浏览器（扩展中继模式）
```javascript
// 启动浏览器
browser({ action: "start", target: "node", node: "wssMac", profile: "mac" })

// 打开网页
browser({ action: "open", target: "node", node: "wssMac", profile: "mac", url: "https://..." })

// 截图
browser({ action: "screenshot", target: "node", node: "wssMac", profile: "mac", targetId: "..." })
```

### Chrome DevTools MCP 模式（推荐用于已登录网站）
```javascript
// 附加到已运行的 Chrome 会话
browser({ action: "start", target: "host", profile: "user" })

// 打开网页
browser({ action: "open", target: "host", profile: "user", url: "https://..." })
```

## 使用规则
| 场景 | 推荐配置 |
|------|---------|
| **已登录网站自动化** | `profile: "user"` (Chrome DevTools MCP) |
| **Mac 浏览器** | `target: "node", node: "wssMac", profile: "mac"` |
| **Linux 隔离浏览器** | `target: "host", profile: "openclaw"` |
