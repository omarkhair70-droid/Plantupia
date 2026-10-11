"""Plantupia interaction study: local-only browser smoke; not a production/API test.

Install playwright and Chromium, then run: python qa_playwright.py
Captures desktop/mobile screenshots under screenshots/.
"""
from pathlib import Path

from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
HTML = (HERE / "index.html").read_text(encoding="utf-8")
SHOTS = HERE / "screenshots"
SHOTS.mkdir(exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1440, "height": 920})
    errors = []
    page.on("pageerror", lambda error: errors.append(str(error)))
    # set_content also works in sandboxes that prohibit navigating to file://.
    # It does not validate persistence across actual page reloads; manual QA does.
    page.set_content(HTML, wait_until="load")
    page.screenshot(path=str(SHOTS / "desktop-empty.png"))

    page.get_by_role("button", name="أنشئ مساحتي الأولى").click()
    page.locator("#space-name").fill("البيت")
    page.get_by_role("button", name="أنشئ المساحة، وبعدها أضيف نبات").click()
    page.locator("#plant-name").fill("ليلى")
    page.locator("#plant-placement").fill("جنب الشباك")
    page.get_by_role("button", name="ابدأ تاريخ النبات").click()
    assert "ليلى" in page.locator("#screen").inner_text()
    page.screenshot(path=str(SHOTS / "desktop-plant.png"))

    page.get_by_role("button", name="سجّل رعاية أو ملاحظة").click()
    page.locator("#care-note").fill("التربة كانت جافة")
    page.locator(".care-chip").filter(has_text="رويت").click()
    assert page.locator("#care-note").input_value() == "التربة كانت جافة"
    page.get_by_role("button", name="7 أيام").click()
    page.get_by_role("button", name="احفظ اللي حصل").click()
    assert "متابعة اختارتها بنفسك" in page.locator("#screen").inner_text()
    page.get_by_role("button", name="الرعاية").click()
    page.get_by_role("button", name="تقدم 7 أيام في النموذج").click()
    assert "موعد المراجعة وصل" in page.locator("#screen").inner_text()
    page.get_by_role("button", name="راجع النتيجة").click()
    page.locator("#outcome-note").fill("الورق شكله أحسن")
    page.get_by_role("button", name="احفظ النتيجة وأقفل المتابعة").click()
    assert "الورق شكله أحسن" in page.locator("#screen").inner_text()

    page.get_by_role("button", name="اسأل عن التغيّرات دي").click()
    page.locator("#ask-input").fill("ورق النبات اصفر")
    page.get_by_role("button", name="إرسال السؤال").click()
    assert "رد توضيحي ثابت" in page.locator("#screen").inner_text()
    page.screenshot(path=str(SHOTS / "desktop-assistant.png"))

    page.get_by_role("button", name="الدائرة").click()
    page.get_by_role("button", name="جرّب كتابة سؤال").click()
    page.locator("#circle-title").fill("هل ده طبيعي؟")
    page.locator("#circle-body").fill("أوراق البوتس عندي اصفرّت")
    page.get_by_role("button", name="شاهد المعاينة قبل أي نشر").click()
    assert "أوراق البوتس" in page.locator("#screen").inner_text()
    assert "مفيش أي محتوى اتبعت" in page.locator("#screen").inner_text()
    page.screenshot(path=str(SHOTS / "desktop-circle.png"))
    assert not errors, f"JavaScript errors: {errors}"

    mobile = browser.new_page(
        viewport={"width": 390, "height": 844},
        device_scale_factor=2,
        is_mobile=True,
        has_touch=True,
    )
    mobile.set_content(HTML, wait_until="load")
    mobile.screenshot(path=str(SHOTS / "mobile-empty.png"))
    mobile.get_by_role("button", name="أنشئ مساحتي الأولى").click()
    mobile.locator("#space-name").fill("بيتي")
    mobile.get_by_role("button", name="أنشئ المساحة، وبعدها أضيف نبات").click()
    mobile.locator("#plant-name").fill("زعتر")
    mobile.get_by_role("button", name="ابدأ تاريخ النبات").click()
    mobile.screenshot(path=str(SHOTS / "mobile-plant.png"))
    mobile.get_by_role("button", name="اسأل عن النبات").first.click()
    assert "DEMO" in mobile.locator("#screen").inner_text()
    mobile.screenshot(path=str(SHOTS / "mobile-assistant.png"))
    browser.close()
print("PASS: J1 care cycle, J2 scripted help, public privacy preview, mobile smoke.")
