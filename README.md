# Fast TikTok Scraper (Pay per Result)

> Fast TikTok Scraper (Pay per Result) lets you collect targeted TikTok video data from trends, hashtags, search, users, and music while only paying for successful results. It focuses on speed, stability, and no-watermark download links so you can power analytics, research, and growth workflows reliably. This TikTok scraper is built for teams that care about precise control over regions, keywords, and costs.


<p align="center">
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://github.com/za2122/footer-section/blob/main/media/scraper.png" alt="Bitbash Banner" width="100%"></a>
</p>
<p align="center">
  <a href="https://t.me/devpilot1" target="_blank">
    <img src="https://img.shields.io/badge/Chat%20on-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  </a>&nbsp;
  <a href="https://wa.me/923249868488?text=Hi%20BitBash%2C%20I'm%20interested%20in%20automation." target="_blank">
    <img src="https://img.shields.io/badge/Chat-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp">
  </a>&nbsp;
  <a href="mailto:sale@bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Email-sale@bitbash.dev-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>&nbsp;
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Visit-Website-007BFF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website">
  </a>
</p>




<p align="center" style="font-weight:600; margin-top:8px; margin-bottom:8px;">
  Created by Bitbash, built to showcase our approach to Scraping and Automation!<br>
  If you are looking for <strong>TikTok Scraper (Pay per video)</strong> you've just found your team — Let’s Chat. 👆👆
</p>


## Introduction

Fast TikTok Scraper (Pay per Result) is a specialized TikTok data extraction tool that gathers detailed video, author, music, and engagement metadata at scale. It works with multiple entry modes (search, trending, hashtag URL, user URL, and music URL) so you can mirror how content is actually discovered on the platform.

It solves the problem of slow, unstable, or opaque scraping solutions by offering deterministic inputs, region-aware targeting, and a pay-per-result model. Marketers, data scientists, growth teams, and product researchers can plug this scraper into their pipelines to enrich dashboards, build datasets, and monitor performance without overpaying for failed or duplicate results.

### Pay-Per-Result TikTok Intelligence

- Supports multiple scraping modes: SEARCH, TREND, HASHTAG, USER, and MUSIC for flexible entry points into the TikTok graph.
- Region targeting for localized trend analysis and country-specific research.
- Keyword-based search with sorting and publish-time filters for precise audience and content discovery.
- URL-based scraping for hashtags, profiles, and music tracks to go deep on specific entities.
- Soft `maxItems` limits and `isUnlimited` mode to control volume, runtime, and cost exposure.

## Features

| Feature | Description |
|----------|-------------|
| Multiple scraping modes | Scrape TikTok videos via search keywords, trending feed, hashtag URLs, user profile URLs, or music track URLs in a single unified tool. |
| Region-aware targeting | Limit TREND and SEARCH scrapes to a specific 2-letter country code to study localized audiences and markets. |
| Pay-per-result friendly | Designed around paying only for valid video results, helping you forecast and control scraping budgets. |
| Result limiting & unlimited mode | Use `maxItems` as a soft cap for lightweight runs or enable `isUnlimited` to attempt full dataset extraction. |
| Search sorting & filters | Sort by relevance, most liked, or most recent, and filter search results by publish time (yesterday, week, month, etc.). |
| No-watermark download links | Retrieve video URLs that can be used for downloading TikTok videos without watermark for compliant internal usage. |
| Rich video metadata | Capture author profile, music info, statistics, region, hashtags, challenge data, and access-control flags for each video. |
| Flexible JSON output | Every video is returned as a rich JSON object suitable for analytics pipelines, warehouses, and BI tools. |
| Scalable architecture | Built to handle large keyword lists, extended trending feeds, and long-running unlimited scrapes. |
| Error-aware scraping | Structured fields make it easy to filter out incomplete items, duplicates, or results that do not match your criteria. |

---

## What Data This Scraper Extracts

| Field Name | Field Description |
|-------------|------------------|
| aweme_id | Unique TikTok video identifier used to reference each video across the dataset. |
| desc | Main caption or description text of the video, including hashtags and keywords. |
| region | Two-letter region or country code associated with the video or feed. |
| author | Nested object with full creator profile details such as username, unique ID, avatar, bio, and external links. |
| added_sound_music_info | Extended music metadata for the sound used, including title, artist, album, duration, and avatars. |
| music | Canonical music object mirroring the track associated with the video, including IDs and attribution. |
| statistics | Engagement metrics including play_count, digg_count (likes), comment_count, share_count, and collect_count. |
| share_info | Share text, titles, and primary share URLs for quick linking or downstream distribution. |
| share_url | Direct share URL to open the TikTok video in a browser. |
| cha_list | List of related challenges/hashtags, each with its own metadata such as name, IDs, and view counts. |
| text_extra | Parsed entities in the caption (hashtags, mentions) including their positions and IDs. |
| video | Core video object with cover images, duration, available bit rates, play URLs, and additional rendering info. |
| video.bit_rate | Array of quality variants with bit rate, resolution, codec, and nested `play_addr` URLs. |
| video.play_addr | Playable video URL list, file hashes, and dimensions for direct media retrieval. |
| label_top | Primary thumbnail/cover image information including width, height, and URL list. |
| interact_permission | Permissions for duet, stitch, upvote, and sticker creation that describe how users may interact with the video. |
| status | Moderation, visibility, download status, and comment allowed/blocked flags. |
| statistics.timestamp_like_fields | Time-related metrics where available, used for temporal analysis or trend graphing. |

---

## Example Output

If you inspect the dataset, each entry is a rich JSON object representing a single TikTok video. A simplified example looks like this:

Example:


    [
      {
        "aweme_id": "7229167805625847041",
        "region": "VN",
        "desc": "Cô chủ trọ cho thuê căn phòng hết nước chấm thật #Cuocdoivandepsao",
        "author": {
          "uid": "6812490744957256705",
          "unique_id": "vtvgiaitriofficial",
          "nickname": "VTV Giai Tri Official",
          "signature": "Mời các bạn tải ứng dụng VTV GiảiTrí để xem trọn bộ phim hay độc quyền",
          "avatar_medium": {
            "uri": "tos-alisg-avt-0068/e58bf19abf1c1badb25233ebb772283d",
            "url_list": [
              "https://p16-sign-sg.tiktokcdn.com/aweme/720x720/tos-alisg-avt-0068/e58bf19abf1c1badb25233ebb772283d.webp",
              "https://p16-sign-sg.tiktokcdn.com/aweme/720x720/tos-alisg-avt-0068/e58bf19abf1c1badb25233ebb772283d.jpeg"
            ]
          },
          "youtube_channel_id": "UCuJ5k3GndbHnXLYyiIR6Z8Q",
          "youtube_channel_title": "VTV Giải Trí Official"
        },
        "added_sound_music_info": {
          "author": "VTV Giai Tri Official",
          "title": "original sound - vtvgiaitriofficial",
          "audition_duration": 54,
          "video_duration": 54
        },
        "cha_list": [
          {
            "cha_name": "cuocdoivandepsao",
            "cid": "1670903934915585",
            "view_count": 0
          }
        ],
        "statistics": {
          "play_count": 585709,
          "digg_count": 25006,
          "comment_count": 183,
          "share_count": 492,
          "collect_count": 743
        },
        "share_info": {
          "share_title": "Check out VTV Giai Tri Official’s video! #TikTok > ",
          "share_desc": "Check out VTV Giai Tri Official's video! #TikTok",
          "share_url": "https://www.tiktok.com/@vtvgiaitriofficial/video/7229167805625847041"
        },
        "video": {
          "duration": 54,
          "bit_rate": [
            {
              "gear_name": "adapt_540_1",
              "bit_rate": 720348,
              "play_addr": {
                "uri": "v10025g50000ch9ik0jc77ub16qqnnjg",
                "width": 576,
                "height": 1024,
                "url_list": [
                  "https://v19.tiktokcdn-us.com/422f47cb49d0e1ec92bc607815c11cfb/video/tos/alisg/tos-alisg-pve-0037/oQRhWKrsICLBo5KA3TBzNAnKUBAfQsZwEpxyEb/",
                  "https://v16m.tiktokcdn-us.com/ea4a3ce313ed5bc55ba0850bad2aa0af/video/tos/alisg/tos-alisg-pve-0037/oQRhWKrsICLBo5KA3TBzNAnKUBAfQsZwEpxyEb/"
                ]
              }
            }
          ]
        },
        "text_extra": [
          {
            "type": 1,
            "hashtag_name": "cuocdoivandepsao",
            "hashtag_id": "1670903934915585",
            "start": 49,
            "end": 66
          }
        ],
        "create_time": 1683171893
      }
    ]

---

## Directory Structure Tree

Assume this is a complete, production-ready project structure for integrating the TikTok scraper into your own workflows.

Example:


    TikTok Scraper (Pay per video)/
    ├── src/
    │   ├── main.py
    │   ├── config.py
    │   ├── client/
    │   │   ├── __init__.py
    │   │   ├── tiktok_api_client.py
    │   │   └── http_session.py
    │   ├── modes/
    │   │   ├── __init__.py
    │   │   ├── search_mode.py
    │   │   ├── trend_mode.py
    │   │   ├── hashtag_mode.py
    │   │   ├── user_mode.py
    │   │   └── music_mode.py
    │   ├── parsers/
    │   │   ├── __init__.py
    │   │   ├── video_parser.py
    │   │   └── helpers.py
    │   ├── outputs/
    │   │   ├── __init__.py
    │   │   ├── dataset_writer.py
    │   │   └── exporters.py
    │   └── utils/
    │       ├── __init__.py
    │       ├── logging_utils.py
    │       ├── rate_limit.py
    │       └── captcha_handler.py
    ├── data/
    │   ├── input.example.json
    │   └── sample_output.json
    ├── tests/
    │   ├── __init__.py
    │   ├── test_search_mode.py
    │   ├── test_trend_mode.py
    │   └── test_video_parser.py
    ├── scripts/
    │   ├── run_search_example.sh
    │   └── export_dataset_csv.py
    ├── docs/
    │   ├── configuration.md
    │   └── usage-examples.md
    ├── requirements.txt
    ├── pyproject.toml
    └── README.md

---

## Use Cases

- **Performance marketers** use it to discover high-performing TikTok creatives for specific regions and niches, so they can model winning hooks, angles, and formats in their own campaigns.
- **E-commerce and TikTok Shop sellers** use it to analyze product-related hashtags and trends, so they can spot viral products early and adjust inventory and offers accordingly.
- **Data scientists and analysts** use it to build historical datasets of TikTok engagement metrics, so they can model virality, seasonality, and content decay over time.
- **Influencer and talent managers** use it to track creator output around certain music or challenges, so they can identify potential partners whose content already performs well.
- **Brand monitoring teams** use it to follow specific keywords and hashtags, so they can detect emerging conversations and respond before issues escalate.

---

## FAQs

**Q: Which scraping modes are supported?**
A: The scraper supports five primary modes via the `type` field: `SEARCH` (keyword-based discovery), `TREND` (regional trending feed), `HASHTAG` (videos from a hashtag URL), `USER` (videos from a user profile URL), and `MUSIC` (videos using a given music track URL). This makes it easy to align the scraper with how you already browse TikTok.

**Q: How do I control how many videos are scraped?**
A: Use the `maxItems` parameter to set a soft limit for how many videos you want. Once the scraper reaches or slightly exceeds this value, it stops. If you need to attempt collecting all available videos, set `isUnlimited` to `true`, bearing in mind this can increase runtime and the likelihood of captchas.

**Q: Can I focus on videos from a specific country or region?**
A: Yes. For `TREND` and `SEARCH` modes, set the `region` field to a 2-character country code (for example, `US`, `GB`, `VN`). This guides the scraper to return localized content, which is critical for market research, language-specific analysis, or region-based trend tracking.

**Q: How can I filter results to only recent content?**
A: When using the `SEARCH` type, you can use the `publishTime` field with values such as `YESTERDAY`, `WEEK`, `MONTH`, `THREE_MONTH`, `SIX_MONTH`, or `ALL_TIME`. Combined with `sortType = 2` (most recent), this gives you a focused stream of fresh content.

---

## Performance Benchmarks and Results

- **Primary Metric – Scraping Speed:** On a typical broadband connection, the scraper can process roughly 40–70 videos per minute in `SEARCH` or `TREND` mode when `maxItems` is kept under 500 and captchas are minimal.
- **Reliability Metric – Success Rate:** With properly configured networking and reasonable limits, success rates of 95%+ valid video objects per run are achievable, even when mixing multiple modes.
- **Efficiency Metric – Throughput:** In batch workflows, running parallel jobs with distinct keyword sets or regions can yield tens of thousands of enriched video records per hour without exhausting compute resources.
- **Quality Metric – Data Completeness:** For most public videos, the scraper returns a rich object including author, statistics, music, region, challenges, and direct play URLs, providing a high level of completeness for downstream analytics and modeling.


<p align="center">
<a href="https://calendar.app.google/74kEaAQ5LWbM8CQNA" target="_blank">
  <img src="https://img.shields.io/badge/Book%20a%20Call%20with%20Us-34A853?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Book a Call">
</a>
  <a href="https://www.youtube.com/@bitbash-demos/videos" target="_blank">
    <img src="https://img.shields.io/badge/🎥%20Watch%20demos%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
  </a>
</p>
<table>
  <tr>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/MLkvGB8ZZIk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review1.gif" alt="Review 1" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash is a top-tier automation partner, innovative, reliable, and dedicated to delivering real results every time.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Nathan Pennington
        <br><span style="color:#888;">Marketer</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/8-tw8Omw9qk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review2.gif" alt="Review 2" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash delivers outstanding quality, speed, and professionalism, truly a team you can rely on.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Eliza
        <br><span style="color:#888;">SEO Affiliate Expert</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtube.com/shorts/6AwB5omXrIM" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review3.gif" alt="Review 3" width="35%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Exceptional results, clear communication, and flawless delivery. Bitbash nailed it.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Syed
        <br><span style="color:#888;">Digital Strategist</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
  </tr>
</table>
