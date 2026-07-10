---
name: seo-content-generation
description: Master protocol for generating highly-optimized, 0% AI-detected SEO content with precisely formatted WebP images.
---

# Master Protocol for SEO Content Generation

You MUST adhere strictly to the following Master Protocol EVERY SINGLE TIME you generate content:

## 1. Keyword Sourcing & Duplicate Prevention
- **Source**: Parse the project's Keyword CSV file and select the highest-volume keywords available (ignore competition metrics).
- **Duplicate Prevention**: ALWAYS cross-reference your selected keywords against the site's existing content or `used_keywords.txt`. You must never write about the same topic twice.

## 2. Content Generation
- **Human-Like Tone**: Write long-form, high-quality articles. The content MUST be written in a highly natural, engaging, and conversational tone to ensure it scores as "0% AI-generated" on AI detectors.
- **Topical SEO**: Cover the topic comprehensively to build Topical Authority within the niche.
- **Semantic SEO**: Utilize NLP entities, LSI keywords, and structured context seamlessly throughout the article.
- **E-E-A-T Guidelines**: Position the content to demonstrate Experience, Expertise, Authoritativeness, and Trustworthiness.
- **Internal Linking**: Ensure absolutely NO internal links point to draft or deleted posts. Only generate internal links to verified, live URLs found in the sitemap to maintain a 0% 404 rate. Interlink strictly based on your approved Topical Map (Spokes pointing to Pillars).

## 3. Image Generation & Processing
- **Image Volume**: Generate exactly 1 Hero/Featured image and 2 to 3 Inline images per article.
- **Precise Sizing & Cropping**: Resize both Hero images and Inline images to exactly `1200x675px`. THEY MUST NOT LOOK STRETCHED. Use Python (e.g., Pillow) to script a "smart center-crop" to a 16:9 ratio before resizing, rather than squashing the image.
- **Formatting & Compression**: Convert all generated images to the `.webp` format and compress them to strictly under 100KB for optimal site speed.
- **Alt Text SEO**: When uploading images to the repository, you MUST ensure that the exact target keyword is included naturally in the Alt Text of every image (especially the Hero image).
