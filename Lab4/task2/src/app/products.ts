export interface Product {
  id: number;
  name: string;
  price: number;
  description: string;
  rating: number;
  image: string;
  addressUrl: string;
  link: string;
}

export const products = [
  {
    id: 1,
    name: 'Смарт-часы Apple Watch',
    price: 119995,
    description: 'Смарт-часы Apple Watch SE 2 Gen (2022) 40 мм midnight',
    rating: 5,
    image: "https://resources.cdn-kaspi.kz/img/m/p/h1c/h70/64533889384478.jpg?format=gallery-medium",
    addresUrl: 'https://kaspi.kz/shop/p/apple-watch-se-2-gen-2022-40-mm-midnight-106362731/?c=196220100#!/item',
    link: "https://wa.me/77478834241?text=https%3A%2F%2Fkaspi.kz%2Fshop%2Fp%2Fapple-watch-se-2-gen-2022-40-mm-midnight-106362731%2F%3Fc%3D196220100%23!%2Fitem"
  },
  {
    id: 2,
    name: 'Наушники',
    price: 16500,
    description: 'Наушники JBL Tune 510BT белый',
    rating: 5,
    image: "https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h3d/h52/33973207105566/jbl-tune-510bt-belyj-101420096-1-Container.jpg",
    addresUrl: 'https://kaspi.kz/shop/p/jbl-tune-510bt-belyi-101420096/?c=196220100#!/item',
    link: "https://wa.me/77478834241?text=https%3A%2F%2Fkaspi.kz%2Fshop%2Fp%2Fjbl-tune-510bt-belyi-101420096%2F%3Fc%3D196220100%23!%2Fitem"
  },
  {
    id: 3,
    name: 'SPF-крем',
    price: 4890,
    description: 'Round Lab крем Birch Juice Moisturizing SPF50+ для лица 50 мл',
    rating: 5,
    image: "https://resources.cdn-kaspi.kz/img/m/p/h58/h4a/64516795826206.jpg?format=gallery-medium",
    addresUrl: 'https://kaspi.kz/shop/p/round-lab-krem-birch-juice-moisturizing-spf50-dlja-litsa-50-ml-105263927/?c=750000000',
    link: "https://wa.me/77478834241?text=https%3A%2F%2Fkaspi.kz%2Fshop%2Fp%2Fround-lab-krem-birch-juice-moisturizing-spf50-dlja-litsa-50-ml-105263927%2F%3Fc%3D750000000"
  },
  {
    id: 4,
    name: 'Apple iPhone 15',
    price: 622916,
    description: 'Смартфон Apple iPhone 15 Pro Max 256Gb серый',
    rating: 5,
    image: "https://resources.cdn-kaspi.kz/img/m/p/hc1/h65/83559848181790.png?format=gallery-medium",
    addresUrl: 'https://kaspi.kz/shop/p/apple-iphone-15-pro-max-256gb-seryi-113138420/?c=750000000',
    link: "https://wa.me/77478834241?text=https%3A%2F%2Fkaspi.kz%2Fshop%2Fp%2Fapple-iphone-15-pro-max-256gb-seryi-113138420%2F%3Fc%3D750000000"
  },
  {
    id: 5,
    name: 'Смартфон Samsung Galaxy',
    price: 120256,
    description: 'Смартфон Samsung Galaxy A23 6 ГБ/128 ГБ черный',
    rating: 5,
    image: "https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/hb5/ha6/49792685244446/smartfon-samsung-galaxy-a23-sm-a235fzkkskz-128gb-black-104348541-1.jpg",
    addresUrl: 'https://kaspi.kz/shop/p/samsung-galaxy-a23-6-gb-128-gb-chernyi-104348541/?c=196220100#!/item',
    link: "https://wa.me/77478834241?text=https%3A%2F%2Fkaspi.kz%2Fshop%2Fp%2Fsamsung-galaxy-a23-6-gb-128-gb-chernyi-104348541%2F%3Fc%3D196220100%23!%2Fitem"
  },
  {
    id: 6,
    name: 'Смартфон Apple iPhone 13',
    price: 294041,
    description: 'Смартфон Apple iPhone 13 128Gb черный',
    rating: 5,
    image: "https://resources.cdn-kaspi.kz/img/m/p/h32/h70/84378448199710.jpg?format=gallery-medium",
    addresUrl: 'https://kaspi.kz/shop/p/apple-iphone-13-128gb-midnight-chernyi-102298404/?c=196220100#!/item',
    link: "https://wa.me/77478834241?text=https%3A%2F%2Fkaspi.kz%2Fshop%2Fp%2Fapple-iphone-13-128gb-midnight-chernyi-102298404%2F%3Fc%3D196220100%23!%2Fitem"
  },
  {
    id: 7,
    name: 'Чехол',
    price: 440,
    description: 'Чехол OEM для Apple iPhone 11 черный',
    rating: 5,
    image: "https://resources.cdn-kaspi.kz/img/m/p/hfd/h5d/63834120978462.jpg?format=gallery-medium",
    addresUrl: 'https://kaspi.kz/shop/p/oem-dlja-apple-iphone-11-chernyi-100335658/?c=750000000',
    link: "https://wa.me/77478834241?text=https%3A%2F%2Fkaspi.kz%2Fshop%2Fp%2Foem-dlja-apple-iphone-11-chernyi-100335658%2F%3Fc%3D750000000"
  },
  {
    id: 8,
    name: 'Ноутбук Apple MacBook Air',
    price: 409990,
    description: 'Ноутбук Apple MacBook Air 13 MGND3 золотистый',
    rating: 5,
    image: "https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/hfd/h54/33286638272542/apple-macbook-air-2020-13-3-mgnd3-zolotistyj-100797576-1-Container.jpg",
    addresUrl: 'https://kaspi.kz/shop/p/apple-macbook-air-13-mgnd3-zolotistyi-100797576/?c=196220100#!/item',
    link: "https://wa.me/77478834241?text=https%3A%2F%2Fkaspi.kz%2Fshop%2Fp%2Fapple-macbook-air-13-mgnd3-zolotistyi-100797576%2F%3Fc%3D196220100%23!%2Fitem"
  },
  {
    id: 9,
    name: 'Планшет Apple iPad',
    price: 414999,
    description: 'Планшет Apple iPad Pro 2022 Wi-Fi 11 дюйм 8 Гб/128 Гб серый',
    rating: 5,
    image: "https://resources.cdn-kaspi.kz/img/m/p/h15/h91/64895796412446.jpg?format=gallery-medium",
    addresUrl: 'https://kaspi.kz/shop/p/apple-ipad-pro-2022-wi-fi-11-djuim-8-gb-128-gb-seryi-107276534/?c=750000000',
    link: "https://wa.me/77478834241?text=https%3A%2F%2Fkaspi.kz%2Fshop%2Fp%2Fapple-ipad-pro-2022-wi-fi-11-djuim-8-gb-128-gb-seryi-107276534%2F%3Fc%3D750000000"
  },
  {
    id: 10,
    name: 'Игрушка',
    price: 1550,
    description: 'Интерактивная игрушка Youmu Toys танцующий кактус мультиколор',
    rating: 4.5,
    image: "https://resources.cdn-kaspi.kz/img/m/p/hd1/hb8/66792868708382.jpg?format=gallery-medium",
    addresUrl: 'https://kaspi.kz/shop/p/interaktivnaja-igrushka-youmu-toys-tantsujuschii-kaktus-mul-tikolor-102651153/?c=750000000',
    link: "https://wa.me/77478834241?text=https%3A%2F%2Fkaspi.kz%2Fshop%2Fp%2Finteraktivnaja-igrushka-youmu-toys-tantsujuschii-kaktus-mul-tikolor-102651153%2F%3Fc%3D750000000"
  },
];