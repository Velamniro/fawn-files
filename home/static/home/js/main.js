document.addEventListener('DOMContentLoaded', () => {
    const select1 = new CustomSelect('#select-1', {
        name: 'Версия', // значение атрибута name у кнопки
        targetValue: 'none', // значение по умолчанию
        options: [['none', 'Выберите версию'], ['1.18.2', '1.18.2'], ['1.16.5', '1.16.5'], ['1.15.2', '1.15.2'], ['1.14.4', '1.14.4'], ['1.12.2', '1.12.2'], ['other', 'Другая']], // опции
        onSelected(select, option) {
            // выбранное значение
            console.log(`Выбранное значение: ${select.value}`);
            // индекс выбранной опции
            console.log(`Индекс выбранной опции: ${select.selectedIndex}`);
            // выбранный текст опции
            const text = option ? option.textContent : '';
            console.log(`Выбранный текст опции: ${text}`);
        },
    });

    const select2 = new CustomSelect('#select-2', {
        name: 'Тип', // значение атрибута name у кнопки
        targetValue: 'none', // значение по умолчанию
        options: [['none', 'Выберите тип'], ['Карта', 'Карта'], ['Мир', 'Мир'], ['Сборка модов', 'Сборка модов'], ['Сборка плагинов', 'Сборка плагинов'], ['Остальное', 'Остальное']], // опции
        onSelected(select, option) {
            // выбранное значение
            console.log(`Выбранное значение: ${select.value}`);
            // индекс выбранной опции
            console.log(`Индекс выбранной опции: ${select.selectedIndex}`);
            // выбранный текст опции
            const text = option ? option.textContent : '';
            console.log(`Выбранный текст опции: ${text}`);
        },
    });

    window.filter1 = select1;
    window.filter2 = select2;
    window.url = window.location.href;
});

function afClick() {
    if (url.indexOf('?') > -1) {
        url = url.split('?')[0]
    }
    window.location = `${url}?version=${filter1.value}&type=${filter2.value}`
}
