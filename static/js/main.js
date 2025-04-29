const grid = document.querySelector(".grid"); // ✅ Just use the grid container
if (grid) {
  new Masonry(grid, {
    itemSelector: ".grid-item",
    gutter: 20,
  });
}

console.log("main.js loaded");
