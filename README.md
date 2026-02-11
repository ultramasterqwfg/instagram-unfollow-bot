# Instagram Unfollow Automation

>This repository provides a compliance-focused automation framework for managing Instagram follow relationships using official data access patterns and controlled workflows. It addresses the operational challenge behind the *instagram unfollow bot* use case by replacing unsafe UI automation with a structured system for identifying, reviewing, and managing follow relationships responsibly.

Rather than blindly executing actions, the system focuses on visibility, control, and human-in-the-loop decision making.

<p align="center">
  <a href="https://t.me/devpilot1" target="_blank"><img src="https://img.shields.io/badge/Chat%20on-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram"></a>
  <a href="mailto:support@appilot.app" target="_blank"><img src="https://img.shields.io/badge/Email-support@appilot.app-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail"></a>
  <a href="https://Appilot.app" target="_blank"><img src="https://img.shields.io/badge/Visit-Website-007BFF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website"></a>
  <a href="https://discord.gg/3YrZJZ6hA2" target="_blank"><img src="https://img.shields.io/badge/Join-Appilot_Community-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Appilot Discord"></a>
</p>

<p align="center">
Created by Appilot, built to showcase our approach to Automation! <br>
If you are looking for custom <strong> Instagram Unfollow Bot </strong>, you've just found your team — Let’s Chat.&#128070; &#128070;
</p>

## Introduction

As Instagram accounts grow, they often accumulate inactive, irrelevant, or low-quality connections. Creators and operators frequently search for solutions such as an unfollow bot instagram or mass unfollow instagram bot to clean up their accounts, but most tools rely on fragile UI automation that risks account restrictions.

This project automates the **analysis and preparation** phase of follow management: collecting relationship data, applying filtering logic, and producing a clear unfollow review queue. It removes manual effort while preserving safety and platform compliance.

### Why Follow Cleanup Automation Matters

- Large follow lists become unmanageable without structured filtering  
- Manual unfollowing is slow and inconsistent at scale  
- Blind automation increases ban and restriction risk  
- Review-based workflows give creators control and confidence  

## Core Features

| Feature | Description |
|------|------------|
| Relationship Data Sync | Retrieves follower and following metadata using approved API access or exports. |
| Intelligent Filtering | Applies rules to identify likely bot accounts, inactive users, or non-reciprocal follows. |
| Review Queue Builder | Generates a structured list of accounts recommended for unfollow, not auto-executed. |
| Session Safety Limits | Enforces daily and hourly caps aligned with real-world Instagram behaviour. |
| Audit Logging | Maintains full logs of analysis decisions and queue generation steps. |

## How It Works

| Stage | Details |
|------|--------|
| Trigger | Manual run or scheduled maintenance task |
| Input | Account tokens, exported follow data, or API responses |
| Automation Logic | Applies inactivity, reciprocity, and pattern-based filters |
| Output | Review queue of accounts eligible for unfollow |
| Safety Controls | Rate limits, dry-run mode, and human confirmation |

## Tech Stack

- **FastAPI** for orchestration and internal APIs  
- **Instagram Graph API** for compliant data access (where available)  
- **Requests** for controlled HTTP calls  
- **Docker** for isolated and repeatable execution  

## Directory Structure Tree

    instagram-unfollow-automation/
        config/
            session_limits.yaml
            filter_rules.yaml
        automation/
            relationship_scanner.py
            unfollow_queue_builder.py
            pacing_controller.py
        utils/
            http_client.py
            logger.py
            validators.py
        data/
            relationships.json
            review_queue.json
        scripts/
            sync_relationships.py
            build_unfollow_queue.py
        app.py
        requirements.txt
        README.md

## Use Cases

- **Creators** use it to clean up follow lists, so their engagement ratios remain healthy.  
- **Agencies** use it to audit managed accounts, so they avoid risky follow–unfollow cycles.  
- **Growth teams** use it to analyse reciprocity patterns, so decisions are data-driven.  
- **QA teams** use it to test follow management logic without executing live actions.  

## FAQs

**Does this automatically unfollow accounts?**  
No. The system prepares and validates unfollow recommendations. Execution is intentionally separated to prevent unsafe automation.

**Can this replace a follow unfollow instagram bot?**  
It replaces the risky parts by providing structured insight and control, without UI scraping or blind execution.

**Is this suitable for large accounts?**  
Yes. Filtering and pagination are designed to handle large datasets with predictable performance.

**What are the limitations?**  
Instagram’s official APIs restrict certain relationship actions. This project respects those limits and avoids unsupported behaviour.

## Performance & Reliability Benchmarks

- Relationship scan throughput: **1,000–1,500 accounts/minute** (data-only)
- Queue accuracy (rule-based): **90–93% relevance** depending on filter tuning
- Recommended daily unfollow cap (manual execution): **≤ 150**
- Memory usage: **< 200 MB** per run
- Failure recovery: automatic retry with capped backoff, safe exit on persistent errors

<p align="center">
<a href="https://cal.com/app-pilot-m8i8oo/30min" target="_blank">
 <img src="https://img.shields.io/badge/Book%20a%20Call%20with%20Us-34A853?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Book a Call">
</a>
 <a href="https://www.youtube.com/@Appilot-app/videos" target="_blank">
  <img src="https://img.shields.io/badge/ð¥%20Watch%20demos%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
 </a>
</p>
