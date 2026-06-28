import { chromium } from 'playwright-extra';
import StealthPlugin from 'puppeteer-extra-plugin-stealth';
chromium.use(StealthPlugin());
const browser = await chromium.launch({ headless: true });
const page = await browser.newPage();
await page.goto('data:text/html,<title>ok</title>');
const result = await page.evaluate(() => ({ title: document.title, webdriver: navigator.webdriver, ua: navigator.userAgent.slice(0, 60) }));
await browser.close();
console.log(JSON.stringify(result));
