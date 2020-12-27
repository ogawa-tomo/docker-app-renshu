<template>
    <section>
        <h1>秘境集落探索ツール（ver.2）</h1>
        <br>
        <a href="https://twitter.com/share?ref_src=twsrc%5Etfw" class="twitter-share-button" data-url="https://search-isolated-villages-2.herokuapp.com/" data-text="秘境集落探索ツール（ver.2）" data-size="large">Tweet</a>
        <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
        <br>
        <div>秘境集落を探索し、秘境度を人口分布データをもとに評価して地域別にランキングで出力します。</div><br>
        <a href="/uranai">秘境集落占い</a><br>

        <div class="dropdown">
        <!--    <a class="btn btn-default dropdown-toggle" href="#" role="button" id="dropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">-->
            <button class="btn btn-light btn-sm dropdown-toggle border-dark" type="button" data-toggle="dropdown">
                その他の秘境探索ツールへ移動
            </button>
            <div class="dropdown-menu" aria-labelledby="dropdownMenuLink">
                <a class="dropdown-item" href="/post_office">秘境郵便局探索ツール</a>
                <a class="dropdown-item" href="/elementary_school">秘境小学校探索ツール</a>
                <a class="dropdown-item" href="/station">秘境駅探索ツール</a>
                <a class="dropdown-item" href="/abandoned_station">秘境廃駅探索ツール</a>
                <a class="dropdown-item" href="/michinoeki">秘境道の駅探索ツール</a>
                <a class="dropdown-item" href="/new_town">秘境ニュータウン探索ツール</a>
                <a class="dropdown-item" href="/research_institute">秘境研究機関探索ツール</a>
            </div>
        </div>

        <img src="/static/village.png" width="350">
        <br><br>
    </section>
</template>