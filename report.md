# 📄 Report — Multi-Agent MCP + A2A System

**Name:** Đoàn Minh Quang  
**Student ID:** 2A202600757  

---

##  1. Objective

Mục tiêu của bài lab là chuyển từ mô hình **single-agent** sang **multi-agent system**, sử dụng:

- **MCP (Model Context Protocol)** → để gọi tool / dữ liệu  
- **A2A (Agent-to-Agent)** → để agent giao tiếp với nhau  

Hệ thống nhằm cải thiện:
- tính modular  
- khả năng mở rộng  
- khả năng trace và debug  

---

##  2. System Architecture

###  2.1 Tổng quan

Hệ thống gồm:

- **Supervisor / Router Agent**
  - nhận input từ user
  - quyết định route task

- **Worker Agents**
  - Customer Agent
  - Law Agent
  - Tax Agent
  - Compliance Agent  

---

###  2.2 Luồng hoạt động

```text
User → Router → (Agent phù hợp)
                ↓
           xử lý task
                ↓
          trả kết quả
```

---

## 🔗 3. MCP Integration

MCP được sử dụng để:
- kết nối agent với tools / data
- chuẩn hóa input / output

Ví dụ:
- truy vấn dữ liệu khách hàng  
- kiểm tra policy  

---

##  4. A2A Communication

Agent giao tiếp thông qua message-based communication:

- Agent không gọi trực tiếp code của nhau  
- Sử dụng task/message để phối hợp  

Ví dụ:
```json
{
  "task": "check_policy",
  "from": "router",
  "to": "compliance_agent"
}
```

---

##  5. Implementation Components

### Agents
- `customer_agent`
- `law_agent`
- `tax_agent`
- `compliance_agent`

###  Core
- `common/llm.py` → xử lý LLM  
- `stages/` → các pipeline (single-agent → multi-agent)  

###  Exercises
- `exercise_4_multiagent.py` → triển khai multi-agent system  

---

##  6. Single vs Multi-Agent

| Tiêu chí | Single Agent | Multi-Agent |
|----------|------------|------------|
| Kiến trúc | Monolithic | Modular |
| Debug | Khó | Dễ trace |
| Mở rộng | Khó | Dễ |
| Performance | Giới hạn | Tối ưu hơn |

---

##  7. Key Improvements

- Tách biệt rõ trách nhiệm từng agent  
- Dễ dàng thêm agent mới  
- Có thể theo dõi flow xử lý  

---

##  8. Conclusion

Hệ thống multi-agent kết hợp MCP + A2A giúp:
- tăng tính linh hoạt  
- giảm độ phức tạp  
- cải thiện khả năng maintain và debug  
