import { add } from './modules/math';

console.log('you are ready to start coding typescript...');

const root = document.createElement('div');
root.id = 'root';
document.body.appendChild(root);

const main = document.createElement('div');
const child = document.createElement('p');
child.innerHTML = 'Hello';
main.appendChild(child);
root.appendChild(main);

// import { sortedItems } from './tests/priceSorter/priceSorter';
// console.log(sortedItems);
import { bestSellers } from './tests/bestSellers/bestSellers';
console.log(bestSellers);
