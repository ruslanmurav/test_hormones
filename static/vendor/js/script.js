const submitButton = document.getElementById("submit-btn");

submitButton.addEventListener("click", function() {
  const testosteroneValue = document.getElementById("testosterone").value;
  // Получите значения других гормонов аналогичным образом

  // Вызов функции для обработки значений гормонов
  processHormoneValues(testosteroneValue);
  // Добавьте вызовы для других гормонов

  // Дополнительные действия при нажатии кнопки "Подтвердить"
});

function processHormoneValues(testosteroneValue) {
  // Здесь вы можете выполнить дополнительные действия с переданными значениями гормонов,
  // например, выводить результаты, анализировать состояние и так далее.
}

function updateOutput(input) {
  const outputId = input.id + '-output';
  const output = document.getElementById(outputId);
  output.value = input.value;
}