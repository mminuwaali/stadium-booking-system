
module.exports = {
    content: [
        '../../**/templates/**/**/*.html',
    ], plugins: [
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
    ],
    theme: {
        extend: {
            scale: {
                '200': '2.0',
                "250": "2.5",
                '300': '3.0',
                '350': '3.5',
                '400': '4.0',
                '450': '4.5',
                '500': '5.0',
            },
            spacing: {
                "1%": "1%",
                "2%": "2%",
                "3%": "3%",
                "4%": "4%",
                "5%": "5%",
                "6%": "6%",
                "7%": "7%",
                "8%": "8%",
                "9%": "9%",
                "10%": "10%",
                "15%": "15%",
                "20%": "20%",
                "25%": "25%",
                "30%": "30%",
                "35%": "35%",
                "40%": "40%",
                "45%": "45%",
                "50%": "50%",
            },
            backgroundImage: {
                "banner-horizontal": "url('/static/images/banner.jpg')",
            }
        },
    },
}
