{-
   Excited without bugs, have fun ("▔□▔)/hi~♡ Nasy.
   -----------------------------------------------
   |
   |             *         *
   |                  .                .
   |           .
   |     *                      ,
   |                   .
   |
   |                               *
   |          |\___/|
   |          )    -(             .              '
   |         =\  -  /=
   |           )===(       *
   |          /   - \
   |          |-    |
   |         /   -   \     0.|.0
   |  NASY___\__( (__/_____(\=/)__+1s____________
   |  ______|____) )______|______|______|______|_
   |  ___|______( (____|______|______|______|____
   |  ______|____\_|______|______|______|______|_
   |  ___|______|______|______|______|______|____
   |  ______|______|______|______|______|______|_
   |  ___|______|______|______|______|______|____

   -----------------------------------------------

   Author              : Nasy https://nasy.moe <Nasy>
   Date                : Mar 10, 2018
   Email               : echo bmFzeXh4QGdtYWlsLmNvbQo= | base64 -D
   Filename            : Views.elm
   Last modified by    : Nasy
   Last modified time  : Mar 10, 2018
   License             : MIT

   -----------------------------------------------

   There are more things in heaven and earth, Horatio, than are dreamt.
      From "Hamlet"
-}


module Views exposing (..)

import Html exposing (..)
import Html.Attributes exposing (..)
import Html.Events exposing (..)
import Json.Encode exposing (string)
import Msgs exposing (Msg)
import Models exposing (BlogModel, BlogsModel, Model, Route(..))
import RemoteData exposing (WebData)
import Date
import Moment


view : Model -> Html Msg
view model =
    div []
        [ header [ id "header", class "header" ] <| header_view model
        , main_ [ id "main" ] <| main_view model
        , footer [ id "footer", class "footer" ] footer_view
        ]



-- Header Views --


header_view : Model -> List (Html Msg)
header_view model =
    let
        hidden =
            case model.settings.route of
                BlogRoute ->
                    True

                _ ->
                    False
    in
        [ section
            [ class "header-section" ]
            [ h1
                [ class "header-section-title main-title" ]
                [ text "Nasy Land"
                ]
            , section [ class "header-section-section" ] <| nav_view "header-section"
            ]
        , section [ class "header-section", classList [ ( "hidden", hidden ) ] ]
            [ p
                [ class "header-section-description description" ]
                [ text "Nasy 栽花，养鱼，闲聊的地方～♡" ]
            ]
        , section [ class "header-section", classList [ ( "hidden", hidden ) ] ] <| find_me "header"
        ]



-- Main Views --


main_view : Model -> List (Html Msg)
main_view model =
    case model.settings.route of
        Normal ->
            [ h2 [ class "main-h2", id "writings" ] [ text "Writings" ]
            , blogs_view model.blogs
            ]

        BlogRoute ->
            [ blog_view model
            , div [ id "gitalk-comment" ]
                [ p [ onClick Msgs.InitComment ]
                    [ text "Click to load comments" ]
                ]
            ]

        NotFoundRoute ->
            [ h2 [ class "main-h2" ] [ text "Main H2 Text Other" ], notfound ]



-- Footer Views --


footer_view : List (Html Msg)
footer_view =
    [ section [ class "footer-section" ] <| nav_view "footer" ++ friend_links "footer"
    , section
        [ class "footer-section copyright" ]
        [ p [ onClick Msgs.Up2Top ] [ text "Copyright © 2018 Nasy" ] ]
    , div [ style [ ( "text-align", "right" ) ], onClick Msgs.Up2Top ]
        [ p
            [ style
                [ ( "position", "fixed" )
                , ( "bottom", "0" )
                , ( "right", "10vw" )
                ]
            ]
            [ i
                [ class "fas fa-rocket fa-lg"
                , title "up to top"
                , attribute "data-fa-transform" "rotate--45"
                ]
                []
            ]
        ]
    ]



-- Not Found--


notfound : Html Msg
notfound =
    section []
        [ h3 [ id "failure" ] [ text "似乎出错了!!!!" ]
        , p [ id "failure" ] [ text "试试刷新？" ]
        , p [ id "failure" ] [ text "Error." ]
        ]



-- Nav View --


nav_view : String -> List (Html Msg)
nav_view base =
    [ nav
        [ class "header-section-nav nav" ]
        [ ul [] <|
            [ li
                [ class <| base ++ "-section-nav-list nav-list" ]
                [ a [ href "https://nasy.me", title "Who is Nasy?" ] [ text "Nasy" ] ]
            , li
                [ class <| base ++ "-section-nav-list nav-list" ]
                [ a [ href "/", title "Blog" ] [ text "Blog" ] ]
            , li
                [ class <| base ++ "-section-nav-list nav-list" ]
                [ a [ href "https://pools.nasy.moe", title "Pools" ] [ text "Pools" ] ]
            , li [ class <| base ++ "-section-nav-list nav-list" ]
                [ a [ href "/blog/2018/05/03/About#About", title "About" ] [ text "About" ] ]
            ]
                ++ [ li
                        [ class <| base ++ "-section-nav-list nav-list" ]
                        [ a [ href "/more", title "More" ] [ text "More" ] ]
                   ]
        ]
    ]


friend_links : String -> List (Html Msg)
friend_links base =
    let
        cc =
            [ class <| base ++ "-section-nav-list nav-list" ]
    in
        [ nav []
            [ ul []
                [ li cc
                    [ a [ href "https://laobubu.net", title "laobubu" ]
                        [ text "Laobubu" ]
                    ]
                ]
            ]
        ]



-- Find Me --


find_me : String -> List (Html Msg)
find_me base =
    [ p []
        [ text "Find me on "
        , a [ href "https://github.com/nasyxx", title "GitHub" ]
            [ icon "fab fa-github" "GitHub" ]
        , text ", "
        , a [ href "https://twitter.com/nasyxx", title "Twitter" ]
            [ icon "fab fa-twitter" "Twitter" ]
        , text " and "
        , a [ href "mailto:nasyxx+nasymoe@gmail.com?Subject=Hi%20Nasy" ]
            [ icon "fas fa-envelope" "Mail" ]
        , text "."
        ]
    ]



-- Blog View --


blog_view : Model -> Html Msg
blog_view model =
    case model.blog of
        RemoteData.NotAsked ->
            div [] [ text "NotAsked" ]

        RemoteData.Loading ->
            p [ class "blog-loading" ] [ text "Loading Blog" ]

        RemoteData.Success blog ->
            section [ id "blog", class "blog" ] <| blog_ blog model.settings.nav

        RemoteData.Failure err ->
            text <| toString err


blog_ : BlogModel -> { f : Bool, n : Bool } -> List (Html Msg)
blog_ blog nav_ =
    let
        last =
            case blog.last of
                "" ->
                    True

                _ ->
                    False

        next =
            case blog.next of
                "" ->
                    True

                _ ->
                    False
    in
        [ header [ class "blog-header" ]
            [ h1 [] [ text blog.title ]
            , section
                [ onClick Msgs.ChangeNavN
                , class "toc-n"
                , style [ ( "cursor", "context-menu" ) ]
                ]
                [ h3 [] [ text "Table of Content" ] ]
            , text_html "section"
                [ class "blog-content-table", classList [ ( "hidden", nav_.n ) ] ]
                blog.content_table
            , div
                [ style
                    [ ( "appearance", "h1" )
                    ]
                , classList
                    [ ( "hidden", True )
                    , ( "h1-fixed", True )
                    , ( "opacity", True )
                    ]
                ]
                [ p
                    [ class "h1 h1-fixed"
                    , onClick Msgs.ChangeNavF
                    , style
                        [ ( "position", "fixed" )
                        , ( "cursor", "context-menu" )
                        , ( "z-index", "3" )
                        ]
                    ]
                    [ text blog.title ]
                , text_html "section"
                    [ class "blog-content-table h1-fixed"
                    , classList [ ( "hidden", nav_.f ) ]
                    , style
                        [ ( "position", "fixed" )
                        , ( "z-index", "2" )
                        , ( "top", "50px" )
                        , ( "border-top", "none" )
                        , ( "box-shadow", "none" )
                        ]
                    ]
                    blog.content_table
                ]
            , tag_view blog
            ]
        , article [ class "blog-article" ]
            [ text_html "section" [ id "blog-content", class "blog-content" ] blog.content
            , section [ id "blog-content-nav" ]
                [ nav []
                    [ ul []
                        [ li
                            [ id "blog-content-nav-last", classList [ ( "hidden", last ) ] ]
                            [ a [ bhref blog.last blog.last_name ] [ text blog.last_name ] ]
                        , li
                            [ id "blog-content-nav-next", classList [ ( "hidden", next ) ] ]
                            [ a [ bhref blog.next blog.next_name ] [ text blog.next_name ] ]
                        ]
                    ]
                ]
            ]
        ]



-- Blogs View --


blogs_view : WebData BlogsModel -> Html Msg
blogs_view res =
    case res of
        RemoteData.NotAsked ->
            div [] [ text "NotAsked" ]

        RemoteData.Loading ->
            p [ class "blogs-list-loading" ] [ text "Loading Blogs List" ]

        RemoteData.Success blogs ->
            section [ id "blogs-list", class "blogs-list" ] <| blogs_list blogs

        RemoteData.Failure err ->
            text <| toString err


blogs_list_single : BlogModel -> List (Html Msg)
blogs_list_single blog =
    [ article [ class "blogs-list-article" ]
        [ header [ class "blogs-list-header" ]
            [ a [ bhref blog.blog_path blog.title ]
                [ h3 [ id blog.title ]
                    [ text blog.title
                    ]
                ]
            ]
        , tag_view blog
        ]
    ]


blogs_list : BlogsModel -> List (Html Msg)
blogs_list blogs =
    List.map blogs_list_single blogs |> List.concat |> List.reverse



-- Tag View --


tag_view : BlogModel -> Html Msg
tag_view blog =
    section [ class "tags", class "blogs-list-tags" ]
        [ section
            [ class "tags-author" ]
            [ icon "fas fa-pencil-alt" "author", span [] [ text blog.author ] ]
        , section
            [ class "tags-time" ]
            [ icon "far fa-calendar-alt" "time"
            , time [ datetime <| blog.datetime ]
                [ text <| date_formatter blog.datetime ]
            ]
        , section
            [ class "tags-summary"
            , class <|
                case blog.summary of
                    "No Summary" ->
                        "hidden"

                    _ ->
                        ""
            ]
            [ icon "fas fa-quote-left" "summary", span [] [ text blog.summary ] ]
        , section
            [ class "tags-categories" ]
            [ icon "fas fa-tags" "categories", tag_list "categories" blog.categories ]
        , section
            [ class "tags-tags" ]
            [ icon "fas fa-hashtag" "tags", tag_list "tag" blog.tags ]
        ]


tag_li : String -> String -> Html Msg
tag_li prefix tag =
    li [ class "tags-list-li" ]
        [ a [ href <| "/" ++ prefix ++ "/" ++ tag, class "tags-list-li-a" ]
            [ text tag ]
        ]


tag_list : String -> List String -> Html Msg
tag_list prefix tags =
    ul [] <| List.map2 tag_li (List.repeat (List.length tags) prefix) tags



-- Utils --


text_html : String -> List (Attribute msg) -> String -> Html msg
text_html node_string attributes html_string =
    node node_string
        ((++)
            [ string html_string |> Html.Attributes.property "innerHTML" ]
            attributes
        )
        []


bhref : String -> String -> Attribute msg
bhref url title =
    href ("/blog/" ++ url ++ "#" ++ title)


icon : String -> String -> Html msg
icon ss tt =
    i [ class <| "icon " ++ ss, title tt ] []


date_formatter : String -> String
date_formatter datestr =
    case Date.fromString datestr of
        Ok date ->
            Moment.format
                [ Moment.MonthNameFirstThree
                , Moment.Text " "
                , Moment.DayOfMonthSuffix
                , Moment.Text ", "
                , Moment.YearNumber
                ]
                date

        _ ->
            ""
